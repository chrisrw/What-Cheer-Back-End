from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
# Create your views here.

# Create a new user. UserSerializerWithToken serializer object is instantiated with the data the user entered into the signup form. Serializer checks whether or not the data is valid. If valid, save the user and return the user's data in the response (which includes the token). 
class UserList(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# any time a user revisits the site, reloads the page, or does anything that causes React to forget its state. React will check if the user has a token stored in the browser, if a token is found, it'll make a request to this view.
@api_view(['GET'])
def current_user(request):

    serializer = UserSerializer(request.user)
    return Response(serializer.data)
