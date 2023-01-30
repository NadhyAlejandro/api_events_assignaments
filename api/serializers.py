from rest_framework import serializers
from api.models import Assignament, Event



class EventSerializer (serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class AssignamentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Assignament
        fields = "__all__"