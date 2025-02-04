from django.contrib import admin
from .models import *


# Register your models here.

class category(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['id','name']


class product(admin.ModelAdmin):
    list_display = ['name','description','price','quantity','category','product_status']
    list_editable = ['price','quantity','product_status']
    search_fields = ['name','price','product_status']
    list_filter = ['product_status']

class orderInline(admin.TabularInline):
    model = Order_Item
    extra = 0
    
class paymentInline(admin.TabularInline):
    list_display = ['id','payment_date','payment_status','payment_method']
    model = Payment
    extra = 0
    
class order(admin.ModelAdmin):
    list_display = ['id','order_status']
    list_editable = ['order_status']
    inlines = [orderInline,paymentInline]
    


admin.site.register(Category,category)
admin.site.register(Product,product)
admin.site.register(Order,order)
admin.site.register(Order_Item)
admin.site.register(Payment)
admin.site.register(Stock)
