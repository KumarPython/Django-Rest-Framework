from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,CreateAPIView
from ..models import Event,Venue
from .serializers import EventSerializer,VenueSerializer
from .permission import IsEventManager,IsVenueOwner
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import OwnLimitOffsetPagination,OwnPageNumberPagination


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['name']
    pagination_class = OwnPageNumberPagination

    # def get_queryset(self):
    #     query=self.request.GET.get['q']
    #     queryset_list=Event.objects.all()
    #     if query:
    #         queryset_list=queryset_list.filter(
    #             Q(name__icontains=query) |
    #             Q(venue__icontains=query ) |
    #             Q(manager__icontains=query) |
    #             Q(desc__icontains=query) |
    #             Q(attendees__icontains=query)
    #         ).distinct()
    #         return queryset_list


class EventDetailAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EventUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated,IsEventManager]


class EventDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated,IsEventManager,IsAdminUser]


class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)
        return

## ---------- Venue ----------


class VenueListAPIView(ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class VenueDetailAPIView(RetrieveAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class VenueUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated,IsVenueOwner]


class VenueDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated,IsVenueOwner,IsAdminUser]


class VenueCreateAPIView(CreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = IsAuthenticated

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return