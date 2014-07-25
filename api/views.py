from rest_framework import viewsets
from models import Message
from api.serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

