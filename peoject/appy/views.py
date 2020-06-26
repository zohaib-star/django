
from django.http import HttpResponse, Http404
from django.template import loader
from .models import A
from django.shortcuts import render

def index(request):
    ac = A.objects.all()
    template = loader.get_template('A/me.html')
    context = {
        'ac':ac,
    }
    return HttpResponse(template.render(context,request))

def details(request, cou_id):
    try:
        c = A.objects.get(pk=cou_id)
    except A.DoesNotExist:
        raise Http404("not avialble")
    return render(request,'A/you.html',{'c':c})

