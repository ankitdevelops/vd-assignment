import time
from collections import defaultdict, deque
from fastapi import FastAPI, HTTPException
from threading import Lock

app = FastAPI()


class RateLimiter:

    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = defaultdict(deque)
        self.locks = defaultdict(Lock)

    def allow_request(self, user_id: str) -> bool:
        current_time = time.time()
        with self.locks[user_id]:
            user_queue = self.user_requests[user_id]

            while user_queue and current_time - user_queue[0] > self.time_window:
                user_queue.popleft()

            if len(user_queue) < self.max_requests:
                user_queue.append(current_time)
                return True
            else:
                return False


rate_limiter = RateLimiter(max_requests=5, time_window=60)


@app.get("/")
async def limited_resource(user_id: str = "23434"):
    if rate_limiter.allow_request(user_id):
        return {"message": "Request allowed", "user_id": user_id}
    else:
        raise HTTPException(
            status_code=429, detail="Too many requests. Please try again later."
        )
