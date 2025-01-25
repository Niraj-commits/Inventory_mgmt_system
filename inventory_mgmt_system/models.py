from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    quantity = models.FloatField(default=0)
    # category_id = models.ForeignKey(Category,on_delete=models.CASCADE,default=0)
    
# class Stock(models.Model):
#     quantity = models.IntegerField(default=0)
#     product_id = models.ForeignKey(Product,models.PROTECT,default=0)

# class Order(models.Model):
#     possible_choices = [('Pending','Pending'),('Completed','Completed'),('Rejected','Rejected'),('Partial',('Partial'))]
    
#     order_status = models.CharField(max_length=50,choices=possible_choices,default='Pending')

# class Order_Items(models.Model):
#     product_id = models.ForeignKey(Product,on_delete=models.CASCADE,default=0)
#     order_id = models.ForeignKey(Order,on_delete=models.PROTECT,default=0)
#     quantity = models.IntegerField(default=0)

# class Payment(models.Model):
#     possible_stats = [('Pending','Pending'),('Completed','Completed'),('Rejected','Rejected'),('Partial',('Partial'))]
#     payment_date = models.DateTimeField(auto_now_add=True)
#     payment_status = models.CharField(max_length=50,choices=possible_stats,default='Pending')
#     payment_method = models.CharField(max_length=50)
    