from django.shortcuts import render
from rest_framework import viewsets, permissions

from author.serializers import AuthorSerializer
from author.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by("id")
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
