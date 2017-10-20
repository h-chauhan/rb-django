from django.db import models

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

class Item(models.Model):
    product = models.ForeignKey(Product)
    quantityh = models.IntegerField(verbose_name="Half Quantity")
    quantityf = models.IntegerField(verbose_name="Full Quantity")
    order = models.ForeignKey(Order)

    def __str(self):
        return str(self.order.pk) + str(self.pk) 

