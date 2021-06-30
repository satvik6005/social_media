from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from first.data import dat
from first.serial import data_serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
# Create your views here.

class data_view(APIView):
    def get(self,requests):
        data_obj=dat('satvik','mastergoyal2001@gmail.com',19)
        serial_obj=data_serializer(data_obj)
        print(serial_obj.data)

        return Response(JSONRenderer().render(serial_obj.data))
    def post(self,requests):
        # print(requests.data)
        # data=io.BytesIO(requests.data)
        # data=JSONParser().parse(data)
        # print(data)
        ser_data=data_serializer(data=requests.data)
        if ser_data.is_valid():
            print(JSONRenderer().render(data=ser_data.data))
        print('recieved')
        return(Response('fuck yu'))
