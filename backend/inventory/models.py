from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from .utils import generate_purchase_order

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    low_stock_limit = models.PositiveIntegerField(default=5)
    vendor_email = models.EmailField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def check_low_stock(sender, instance, **kwargs):
    if instance.quantity < instance.low_stock_limit:
        print(f"⚠️ Low stock alert for {instance.name}!")

        # Generate PDF
        pdf_path = generate_purchase_order(instance)

        # Send Email
        email = EmailMessage(
            subject="Purchase Order - Low Stock Alert",
            body=f"Stock is low for {instance.name}. Please find attached purchase order.",
            from_email="your_email@gmail.com",
            to=[instance.vendor_email],
        )

        email.attach_file(pdf_path)
        email.send()

        print("📧 Email sent with Purchase Order!")