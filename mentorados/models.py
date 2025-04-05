from django.db import models


class Mentorados(models.model):
    nome = models.CharField(max_length=255)
    