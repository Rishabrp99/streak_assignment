from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .serializer import Orderserializer
from .models import Order
from . import api
# Create your views here.

class OrderApiView(APIView):
    def post(self,request):
        serializer=Orderserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            item= Order.objects.filter().first()
            data={
                "order_id":item.id,
                "order_amount":item.order_amount,
                "payment_url":""
            }
            return Response({"status":"Success","data":data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.data},status=status.HTTP_400_BAD_REQUEST)




    def get(self, request, id=None):
        try:
            item= Order.objects.get(id=id)
            #serializer = Orderserializer(item)
            return Response({"order_id":item.id,"status": "success"}, status=status.HTTP_200_OK)
        except :
            item=None
            return Response({"status":"Failed","Details":"Id not found"},status=status.HTTP_404_NOT_FOUND)

        
