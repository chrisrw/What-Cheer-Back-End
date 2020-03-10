from rest_framework import serializers, generics, permissions
from .models import Entry, Prompt
from django.contrib.auth.models import User

# Entry information including a month-date-year format and linking user to entries
class EntrySerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%m-%d-%Y", input_formats=['%m-%d-%Y', 'iso-8601'])
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Entry
        fields = ('id', 'date', 'entry', 'owner',)

class PromptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prompt
        fields = ('id', 'prompt',)

