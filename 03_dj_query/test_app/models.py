from django.db import models
from django.utils import timezone
from django.db.models import Sum


class Order(models.Model):
    customer = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def top_customers_last_6_months(cls):
        six_months_ago = timezone.now() - timezone.timedelta(days=6 * 30)
        top_customers = (
            cls.objects.filter(order_date__gte=six_months_ago, status="Delivered")
            .values("customer")
            .annotate(total_spent=Sum("total_amount"))
            .order_by("-total_spent")[:5]
        )
        return top_customers

    def __str__(self) -> str:
        return self.customer
