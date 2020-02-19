from django.db import models
from kuras.shared.models import BaseModel


class Season(BaseModel):
    name = models.CharField(max_length=255)
    teams = models.ManyToManyField("teams.Team")
