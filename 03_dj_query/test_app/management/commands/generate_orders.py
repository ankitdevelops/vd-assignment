from django.core.management.base import BaseCommand
from faker import Faker
from test_app.models import Order
import random
from django.utils import timezone


class Command(BaseCommand):
    help = "Generate dummy orders"

    def handle(self, *args, **kwargs):
        fake = Faker()
        customers = [
            "Customer A",
            "Customer B",
            "Customer C",
            "Customer D",
            "Customer E",
            "Customer F",
            "Customer G",
            "Customer H",
            "Customer I",
            "Customer J",
        ]
        status_choices = ["Pending", "Shipped", "Delivered", "Cancelled"]

        for _ in range(100):
            customer = random.choice(customers)
            order_date = fake.date_time_between(
                start_date="-6M", end_date="now", tzinfo=timezone.get_current_timezone()
            )
            status = random.choice(status_choices)
            total_amount = round(random.uniform(50, 1000), 2)

            Order.objects.create(
                customer=customer,
                order_date=order_date,
                status=status,
                total_amount=total_amount,
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully generated 100 dummy orders.")
        )
