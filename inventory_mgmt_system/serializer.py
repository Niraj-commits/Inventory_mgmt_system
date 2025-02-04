from rest_framework.response import Response
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
    def create(self,validated_data):
        occurences = self.Meta.model.objects.get(name = validated_data.get('name')).count()
        
        if occurences > 0:
            raise serializers.ValidationError("Category already exist")
        
        category = self.Meta.model(**validated_data)
        category.save()
        return category
    
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.get(name = validated_data.get('name')).count()
        
        if occurences > 0:
            raise serializers.ValidationError("Category already exist")
        
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','quantity','category','product_status']
        
    def create(self,validated_data):
        occurences = self.Meta.model.objects.get(name = validated_data.get('name'),category = validated_data.get('category')).count()
        
        if occurences > 0:
            raise serializers.ValidationError("Category already exist")
        
        product = self.Meta.model(**validated_data)
        product.save()
        return product
    
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.get(name = validated_data.get('name'),category = validated_data.get('category')).count()        
        if occurences > 0:
            raise serializers.ValidationError("Category already exist")
        
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','quantity','product_id']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','order_status']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = ['id','product','order','quantity']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','date','status','payment_method','order']