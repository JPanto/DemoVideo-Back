from .models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, StateEventSerializer, EventSkillSerializer, EventUserSerializer


class EventAPI(APIView):
    """ Basic API Event """

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


class EventUserAPI(APIView):
    """ API Event User """
    pass
