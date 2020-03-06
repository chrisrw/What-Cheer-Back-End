from rest_framework import serializers, generics, permissions
from .models import Entry, Prompt
from django.contrib.auth.models import User
class EntrySerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Entry
        fields = ('id', 'date', 'entry', 'user_id')

class PromptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prompt
        fields = ('id', 'prompt')

