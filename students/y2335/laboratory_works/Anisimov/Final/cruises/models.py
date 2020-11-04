from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MotorshipTeam(models.Model):
    team_id = models.IntegerField()

class Motorship(models.Model):
    motorship_id = models.IntegerField()
    motorship_name = models.CharField(max_length=45)
    motorship_date_start = models.DateField()
    motorship_date_end = models.DateField()
    team = models.ManyToManyField(MotorshipTeam)

    def __str__(self):
        return  "%s" % self.motorship_name

class Sailor(models.Model):
    sailor_id = models.IntegerField()
    sailor_name = models.CharField(max_length=45)
    sailor_lastName = models.CharField(max_length=45)
    team = models.ManyToManyField(MotorshipTeam)

class Cruis(models.Model):
    cruis_id = models.IntegerField()

class Tour(models.Model):
    tour_id = models.IntegerField()
    tour_datetime = models.DateTimeField()
    cruis = models.ManyToManyField(Cruis)
    motorship = models.ForeignKey(Motorship, on_delete=models.DO_NOTHING)

class Route(models.Model):
    route_id = models.IntegerField()
    route_days = models.IntegerField()
    rote_stops = models.IntegerField()
    rote_begin = models.CharField(max_length=45)
    rote_end = models.CharField(max_length=45)

class CruisRoute(models.Model):
    route = models.ManyToManyField(Route)
    cruis = models.ManyToManyField(Cruis)

class TicketCategory(models.Model):
    category_name = models.CharField(default="Category", max_length=45)
    category_id = models.IntegerField()
    category_cost = models.IntegerField()

    def __str__(self):
        return  "%s" % self.category_name

class Ticket(models.Model):
    ticket_id = models.IntegerField()
    user_id = models.IntegerField(default=0)
    ownername = models.CharField("Ваше имя", max_length=45, default=" ")
    category = models.ForeignKey(TicketCategory, on_delete=models.DO_NOTHING)
    tour = models.ForeignKey(Tour, on_delete=models.DO_NOTHING)