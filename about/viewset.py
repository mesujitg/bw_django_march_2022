from rest_framework import viewsets
from about.models import About
from about.serializer import AboutSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
