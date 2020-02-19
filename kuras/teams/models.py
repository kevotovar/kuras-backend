from django.db import models

from kuras.users.models import User
from kuras.shared.models import BaseModel


class Team(BaseModel):
    name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name="teams", through="teams.TeamUser")


class TeamUser(BaseModel):
    MEMBER = "member"
    CAPTAIN = "captain"

    ROLE_CHOICES = (
        (MEMBER, "miembro"),
        (CAPTAIN, "capitan"),
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default=MEMBER)
