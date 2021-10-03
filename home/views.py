from django.shortcuts import render

# Create your views here.
from .models import (
    About,
    Skill,
    Service,
)


def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()

    context = {'about': about, 'skills': skills,
               'services': services}
    return render(request, 'home/index.html', context)
