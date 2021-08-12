from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# this class contains data format as a class that would be serialized
# if we have to save the data we can use models instead
from first.data import dat
from first.serial import data_serializer,account_serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
#token table  with foreign key relationship to the users table
from rest_framework.authtoken.models import Token

# Create your views here.
#you can name your views here with genric functionality like form view
# or login view add delete view with all get post type requests
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
# registration class contains all functions related to user registration
class reg(APIView):
    def get(self,requests):
        pass
        
    def post(self,requests):
        serializer=account_serializer(data=requests.data)
        data={}
        if serializer.is_valid():
            
            acc=serializer.save()
            
            data['email']=acc.email
            data['username']=acc.username
            token=Token.objects.get(user=acc).key
            data['token']=token
        
        else:
            data=serializer.errors
        return Response(data)

#authentication class contains all the functions related to authentication
#  class authentication_class(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)

#save method will signal this function to make toke for the registered user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        c=Token.objects.create(user=instance)
        print(c)

#steps for authentication
#1 database table for token foreign key relationship with account table
#url=api/account/login
#genrate a token 
#put it inot the token table
# once they have that they would attach in the header of the request
#then their will be functions to check weather the token is right or not