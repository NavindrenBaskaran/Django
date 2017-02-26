from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello World")


def creator(request):
    return HttpResponse("This site is created by Navindren")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, "current_datetime.html", {'current_datetime': now})

def current_datetime_ ():
    now = datetime.datetime.now()
    return now

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = current_datetime_() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)
