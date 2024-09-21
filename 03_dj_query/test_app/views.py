from django.shortcuts import render
from .models import Order


def top_customers_view(request):
    # Get top customers
    top_customers = Order.top_customers_last_6_months()

    # Render the data to the template
    return render(request, "top_customers.html", {"top_customers": top_customers})
