from rest_framework.response import Response
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
    def create(self,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name')).exists()
        
        if occurences:
            raise serializers.ValidationError("Category already exist")
        
        category = self.Meta.model(**validated_data)
        category.save()
        return category
    
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name')).exists()
        
        if occurences:
            raise serializers.ValidationError("Category already exist")
        
        instance.__dict__.update(validated_data)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    
    vat_price = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category'
    )
    
    class Meta:
        model = Product
        fields = ['id','name','description','price','vat_price','quantity','category',"category_id",'product_status']
    
    def get_vat_price(self,product : Product):
        return product.price * 0.13 + product.price    
        
    def create(self,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name'),category = validated_data.get('category')).exists()
        
        if occurences:
            raise serializers.ValidationError("Product already exist")
        
        product = self.Meta.model(**validated_data)
        product.save()
        return product
    
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name'),category = validated_data.get('category')).exists()        
        if occurences:
            raise serializers.ValidationError("Category already exist")
        
        instance.__dict__.update(validated_data)
        instance.save()
        return instance
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','quantity','product_id']
        


class OrderItemSerializer(serializers.ModelSerializer):
    
    product= serializers.StringRelatedField()
    class Meta:
        model = Order_Item
        fields = ['id','product','order','quantity']
        
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    items = OrderItemSerializer(many = True)
    class Meta:
        model = Order
        fields = ['id','user','order_status','items']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','date','status','payment_method','order']