from django.db import models
import smtplib

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=80)
    priceh = models.IntegerField(verbose_name="Half Price")
    pricef = models.IntegerField(verbose_name="Full Price")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    username = models.CharField(max_length=80)
    phone = models.BigIntegerField()
    type = models.CharField(max_length=80)
    address = models.TextField()
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('rajbhog.r@gmail.com', 'admin@1234')
        msg = "\r\n".join([
            "From: rajbhog.r@gmail.com",
            "To: rajbhog.r@gmail.com",
            "Subject: New Order Received",
            "",
            "A new order has been received. Please check control panel."
        ])
        server.sendmail('rajbhog.r@gmail.com', 'rajbhog.r@gmail.com', msg)
        super(Order, self).save(*args, **kwargs)

class Item(models.Model):
    product = models.ForeignKey(Product)
    quantityh = models.IntegerField(verbose_name="Half Quantity")
    quantityf = models.IntegerField(verbose_name="Full Quantity")
    order = models.ForeignKey(Order)

    def __str(self):
        return str(self.order.pk) + str(self.pk) 

