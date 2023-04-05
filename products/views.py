from django.shortcuts import render
from .models import Products
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from .serializers import ProductSerializer
# Create your views here.
from django_ratelimit.decorators import ratelimit


@api_view(['GET'])
@ratelimit(key='ip', rate='5/m',  method='GET',block=False) #block=true to implement this
def get_products(request):
    search = request.GET.get('search')
    if len(search)==0:
        objects = Products.objects.all().values('name','description','ratings','image','mrp','disc','sale_price')
        # ser_data = ProductSerializer(objects,many=True)
        # print(ser_data.data)
    objects = Products.objects.filter(Q(description__icontains=search) | Q(name__icontains=search)).values('name','description','ratings','image','mrp','disc','sale_price')
    return Response({"data":objects},status=200)
