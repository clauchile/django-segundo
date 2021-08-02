from django.shortcuts import render, HttpResponse
from time import gmtime, localtime, strftime
from django.utils import timezone


def index(request):
    return HttpResponse("<h1>this is the equivalent of @app.route<h1/>")

# Create your views here.

    
def index(request):
    context = {
        "msj": "La fecha y la hora es:",
        "time": strftime(f"%B, %d  %H:%M %p", localtime())
    }
    print(timezone.now(),timezone.localdate())
    return render(request,'index.html', context)


