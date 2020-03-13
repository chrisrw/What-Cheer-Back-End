from rest_framework import serializers, generics, permissions
from .models import Entry, Prompt
from django.contrib.auth.models import User

# Entry information including a month-date-year format and linking user to entries
class EntrySerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Entry
        fields = ('id', 'date', 'entry', 'owner', 'image')

class PromptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prompt
        fields = ('id', 'prompt',)

