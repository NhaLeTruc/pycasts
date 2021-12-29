#from django.views.generic import ListView
from .models import Episode
from django.shortcuts import render
from django.http import HttpResponse

def get_context_data(request):
    #context = super().get_context_data(**kwargs)
    latest_episodes = Episode.collection.order("-pub_date").fetch(10)
    context = {'episodes' : latest_episodes}
    template = render(request,'homepage.html',context)
    response = HttpResponse(template)
    response["Cache-Control"] = "public, max-age=300, s-maxage=600"
    return response