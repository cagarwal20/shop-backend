from django.shortcuts import render
from .models import Products
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q 
#from django.db import models as dmodels
from .serializers import ProductSerializer
# Create your views here.
from django_ratelimit.decorators import ratelimit


@api_view(['GET'])
@ratelimit(key='ip', rate='5/m',  method='GET',block=False) #block=true to implement this
def get_products(request):
    filters = Q()
    params = request.GET
    if "search" in params:
        search = params.get('search')
        filters&=Q(Q(description__icontains=search) | Q(name__icontains=search))
    if "categories" in params:
        categories = params.get('categories')
        filters&=Q(Q(description__icontains=search) | Q(name__icontains=search))
    if "sort_by" in params:
        sort_by = params.get('sort_by')
        if sort_by=="1": #price low to high
            objects = Products.objects.filter(filters).values('name','description','ratings','image','mrp','disc','sale_price').order_by('sale_price')
        if sort_by=="2": #price high to low
            objects = Products.objects.filter(filters).values('name','description','ratings','image','mrp','disc','sale_price').order_by('-sale_price')
        if sort_by=="3": #discount low to high
            objects = Products.objects.filter(filters).values('name','description','ratings','image','mrp','disc','sale_price').order_by('disc')
        if sort_by=="4":
            objects = Products.objects.filter(filters).values('name','description','ratings','image','mrp','disc','sale_price').order_by('-disc')
        return Response({"data":objects},status=200)
    # objects = Products.objects.filter(filters).values('name','description','ratings','image','mrp','disc','sale_price')
    # # if len(search)==0:
    # #     objects = Products.objects.all().values('name','description','ratings','image','mrp','disc','sale_price')
    # #     # ser_data = ProductSerializer(objects,many=True)
    # #     # print(ser_data.data)
    # # objects = Products.objects.filter(Q(description__icontains=search) | Q(name__icontains=search)).values('name','description','ratings','image','mrp','disc','sale_price')
    # return Response({"data":objects},status=200)
