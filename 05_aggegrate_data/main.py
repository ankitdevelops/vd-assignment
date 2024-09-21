from typing import List, Dict, Callable
from collections import defaultdict


def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = defaultdict(list)

    for item in data:
        if key in item:
            grouped_data[item[key]].append(item)

    result = {}
    for group_key, group_items in grouped_data.items():
        result[group_key] = aggregator(group_items)

    return result


data = [
    {"product": "apple", "category": "fruit", "price": 50, "quantity": 10},
    {"product": "banana", "category": "fruit", "price": 30, "quantity": 15},
    {"product": "carrot", "category": "vegetable", "price": 45, "quantity": 8},
    {"product": "date", "category": "fruit", "price": 80, "quantity": 5},
    {"product": "eggplant", "category": "vegetable", "price": 100, "quantity": 3},
]


def total_sales(items):
    return sum(item["price"] * item["quantity"] for item in items)


result = aggregate_data(data, "category", total_sales)

print(result)
