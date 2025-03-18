from django.shortcuts import render,HttpResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework import status
from rest_framework import viewsets
from .paginator import *
from .permission import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters
from .filter import *
# Create your views here.


class CategoryDetails(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    permission_classes = [AllowView]
        
# By using View Sets
class ProductDetails(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowView]
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = customFilter

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
    

class OrderDetails(viewsets.ModelViewSet):
    
    queryset = Order.objects.prefetch_related('items').all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAuthenticated]
    
    
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