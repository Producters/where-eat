from django.db import models
from datetime import date
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    menu = models.TextField()

    def __str__(self):
        return self.name


class VoteManager(models.Manager):

    def todays_votes(self, restaurant):
        return self.get_queryset().filter(restaurant=restaurant, date_voted=date.today())

    def users_todays_votes(self, user):
        return self.get_queryset().filter(date_voted=date.today(), user=user)

class Vote(models.Model):
    restaurant = models.ForeignKey("Restaurant", related_name='votes')
    date_voted = models.DateField(auto_now_add=True)
    user = models.ForeignKey("auth.User")

    objects = VoteManager()