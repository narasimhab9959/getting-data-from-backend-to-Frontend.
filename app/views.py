from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    return render(request,'display_topics.html',d)

def display_webpage(request):
    Webpages=Webpage.objects.all()
    d={'Webpages':Webpages}

    return render(request,'display_webpage.html',d)

def display_AccessRecord(request):
    AccessRecords=AccessRecord.objects.all()
    d={'AccessRecords':AccessRecords}

    return render(request,'display_AccessRecord.html',d)


   