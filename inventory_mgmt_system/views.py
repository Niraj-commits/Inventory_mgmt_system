from django.shortcuts import render,HttpResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework import status
from rest_framework import viewsets
from .paginator import *
from .permission import IsAuthenticatedOrReadOnly
# Create your views here.


class CategoryDetails(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
# By Using  viewsets
# class CategoryDetails(viewsets.ViewSet):
#     pagination_class = CustomPagination 
#     def list(self,request):
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset,many = True)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
            
#     def retrieve(self,request,pk):
#         queryset = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(queryset)
#         return Response(serializer.data)
    
#     def destroy(self,request,pk):
#         queryset = Category.objects.get(pk = pk)
#         occurences = Product.objects.filter(category = queryset).count()
        
#         if occurences > 0:
#             return Response({"Details":"Sorry The data is used"},status=status.HTTP_200_OK)
        
#         else:
#             queryset.delete()
#             return Response({"Details":"Data has been deleted"},status=status.HTTP_200_OK)
    
#     def update(self,request,pk):
#         queryset = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(queryset,data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
    
# By using View Sets
class ProductDetails(viewsets.ViewSet):
    def list(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        queryset = Product.objects.all()
        serializers = ProductSerializer(data = request.data)
        serializers.is_valid(raise_exception=True)
        return Response({"Details":"Data has been added"},status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk):
        queryset = Product.objects.get(pk = pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)
         
    def update(self,request,pk):
        queryset = Product.objects.get(pk = pk)
        serializer = ProductSerializer(queryset, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
    def destroy(self,request,pk):
        queryset = Product.objects.get(pk = pk)
        occurences = Order_Item.objects.filter(product_id = queryset).count()
        
        if occurences > 0:
            return Response({"Details":"Data is used"},status=status.HTTP_226_IM_USED)
        else:
            queryset.delete()
            return Response({"Details":"Data has been deleted"})
        

class StockDetails(viewsets.ViewSet):
    
    def list(self,request):
        queryset = Stock.objects.all()
        serializer = StockSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = StockSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        queryset = Stock.objects.get(pk = pk)
        serializer = StockSerializer(queryset)
        return Response(serializer.data)
    
    def update(self,request,pk):
        queryset = Stock.objects.get(pk = pk)
        serializer = StockSerializer(queryset,data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
    def destroy(self,request,pk):
        queryset = Stock.objects.get(pk = pk)
        queryset.delete()
        return Response({"Details":"Data has been deleted"},status=status.HTTP_200_OK)
    

class OrderDetails(viewsets.ViewSet):
    def list(self,request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = OrderSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        queryset = Order.objects.get(pk = pk)
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)
    
    def update(self,request,pk):
        queryset = Order.objects.get(pk = pk)
        serializer = OrderSerializer(queryset,data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
    def destroy(self,request,pk):
        queryset = Order.objects.get(pk = pk)
        queryset.delete()
        return Response({"Details":"Data has been deleted"},status=status.HTTP_200_OK)

class OrderItemDetails(viewsets.ViewSet):
    def list(self,request):
        queryset = Order_Item.objects.all()
        serializer = OrderItemSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = OrderItemSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        queryset = Order_Item.objects.get(pk = pk)
        serializer = OrderItemSerializer(queryset)
        return Response(serializer.data)
    
    def update(self,request,pk):
        queryset = Order_Item.objects.get(pk = pk)
        serializer = OrderItemSerializer(queryset,data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
    def destroy(self,request,pk):
        queryset = Order_Item.objects.get(pk = pk)
        queryset.delete()
        return Response({"Details":"Data has been deleted"},status=status.HTTP_200_OK)

class PaymentDetails(viewsets.ViewSet):
    def list(self,request):
        queryset = Payment.objects.all()
        serializer = PaymentSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = PaymentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        queryset = Payment.objects.get(pk = pk)
        serializer = PaymentSerializer(queryset)
        return Response(serializer.data)
    
    def update(self,request,pk):
        queryset = Payment.objects.get(pk = pk)
        serializer = PaymentSerializer(queryset,data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
    def destroy(self,request,pk):
        queryset = Payment.objects.get(pk = pk)
        queryset.delete()
        return Response({"Details":"Data has been deleted"},status=status.HTTP_200_OK)