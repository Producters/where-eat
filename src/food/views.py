from django.shortcuts import render, redirect
from food.models import Restaurant, Vote
from django.http import HttpResponse
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index_page(request):

    context = {
        "restaurants": Restaurant.objects.all()
    }

    return render(request, "food/index.html", context)

@login_required
def vote(request, restaurant_id):
    restaurant_id = int(restaurant_id)

    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        return HttpResponse(status=404)

    Vote.objects.users_todays_votes(request.user).delete()

    vote = Vote()
    vote.restaurant = restaurant
    vote.user = request.user
    vote.save()

    return redirect('index')

