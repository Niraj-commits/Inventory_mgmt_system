from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    prod_stat = [('Available','Available'),('Out','Out')]
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    quantity = models.FloatField(default=0)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    product_status = models.CharField(max_length=50,choices=prod_stat,default='Available')
    
    def __str__(self):
        return self.name
    
class Stock(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT,default=None)
    quantity = models.FloatField(default=0)

class Order(models.Model):
    possible_choices = [('Pending','Pending'),('Completed','Completed'),('Rejected','Rejected'),('Partial',('Partial'))]
    order_status = models.CharField(max_length=50,choices=possible_choices,default='Pending')

class Order_Item(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT,default=None)
    order = models.ForeignKey(Order,on_delete=models.PROTECT,default=None)
    quantity = models.IntegerField(default=0)

class Payment(models.Model):
    possible_stats = [('Pending','Pending'),('Completed','Completed'),('Rejected','Rejected'),('Partial',('Partial'))]
    pay_method = [('Esewa','Esewa'),('Khalti','Khalti')]
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=possible_stats,default='Pending')
    payment_method = models.CharField(max_length= 50,choices=pay_method,default='Esewa')
    order = models.ForeignKey(Order,on_delete=models.PROTECT,default=None)
    