from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Allcourse
# Create your views here.
def course(request):
    ac= Allcourse.objects.all()
    template= loader.get_template('eduapp1/course.html')
    context= {
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request, couse_id):
    try:
        course=Allcourse.objects.get(pk=couse_id)
    except Allcourse.DoesNotExist:
        raise Http404('the page u r looking is not available buddy')

    return render(request, 'eduapp1/details.html',{'course':course}) 
