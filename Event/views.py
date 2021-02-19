from .models import Event, StateEvent, EventUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, StateEventSerializer, EventUserSerializer, EventFullSerializer


class EventAPI(APIView):
    """ API Event """

    def post(self, request):
        """" Create Events """
        event_json = EventSerializer(data=request.data) # Unmarshal
        if event_json.is_valid():
            event_json.save()
            return Response(event_json.data, status=201)
        return Response(event_json.errors, status=400)


class EventList(APIView):
    """ Query API Event """

    def get(self, request):
        """ Event List """
        events = Event.objects.all()
        event_json = EventSerializer(events, many=True)
        return Response(event_json.data)


class EventDetail(APIView):
    """ Detail Event """

    def get(self, request, pk):
        """" Event Detail """
        event = Event.objects.get(pk=pk)
        event_json = EventSerializer(event)
        return Response(event_json.data, status=200)


class EventStateList(APIView):
    """ Query API Event States """

    def get(self, request):
        """ Event States List """
        event_states = StateEvent.objects.all()
        event_json = StateEventSerializer(event_states, many=True)
        return Response(event_json.data, status=200)


class EventUserAPI(APIView):
    """ API Event User: Entries"""

    def post(self, request):
        """ Create Entry """
        event_user_json = EventUserSerializer(data=request.data)
        if event_user_json.is_valid():
            event_user_json.save()
            return Response(event_user_json.data, status=201)
        return Response(event_user_json.errors, status=400)

    def get(self, request):
        """ Get all entries """
        event_users = EventUser.objects.all()
        event_user_json = EventUserSerializer(event_users, many=True)
        return Response(event_user_json.data, status=200)


