from django.db import models
from django.db.models import CharField


class Author(models.Model):
    name = CharField(max_length=50, blank=False)
    description = CharField(max_length=200, blank=False)
    books = CharField(max_length=200, blank=False)
    generos = CharField(max_length=200, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.description}"
