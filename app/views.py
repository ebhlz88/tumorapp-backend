from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
# from .serializers import imageserializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from rest_framework import generics

from .serializers import CimageSerializer
from .models import cameraimage
from .utils import Util

class GoogleLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8080"
    client_class = OAuth2Client

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User

class callphotopost(APIView):
    def get(self,request,usrname):
        usrname = usrname.lower()
        allphoto = cameraimage.objects.filter(username__username=usrname)
        allphoto_serializer = CimageSerializer(allphoto,many=True)
        return Response(allphoto_serializer.data)

    parser_classes = [FormParser,MultiPartParser]
    def post(self, request,usrname):   
        usrname = usrname.lower()
        hh = User.objects.get(username=usrname)
        insimage = cameraimage(username=hh)
        image_serialized = CimageSerializer(insimage,data=request.data)
        if image_serialized.is_valid():
            image_serialized.save()
            return Response(image_serialized.data, status=status.HTTP_201_CREATED)
        return Response(image_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

import secrets
from rest_framework.decorators import api_view

@api_view()
def sendemail(self,em):
    print(em)
    code = str(secrets.randbits(20))
    data = {'email_body': 'Your verification code is here \n code: '+code, 'to_email': em,
            'email_subject': 'Verify your email'}
    Util.send_email(data)

    

    return Response({"code":code})


