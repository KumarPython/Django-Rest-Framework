from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from ..models import Event,Venue
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username']


class EventSerializer(ModelSerializer):
    url=HyperlinkedIdentityField(view_name='event-api:detail',lookup_field='pk')
    manager=SerializerMethodField()
    venue=SerializerMethodField()
    attendees=UserSerializer(many=True, read_only=True)

    class Meta:
        model=Event
        fields='__all__'

    def get_manager(self,obj):
        return obj.manager.username

    def get_venue(self,obj):
        return obj.venue.name


class VenueSerializer(ModelSerializer):
    class Meta:
        model=Venue
        fields='__all__'
