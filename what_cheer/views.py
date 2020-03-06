from rest_framework import generics, permissions
from .serializers import EntrySerializer, PromptSerializer, UserSerializer, UserSerializerWithToken
from .models import Entry, Prompt
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

class PromptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [permissions.IsAuthenticated]

