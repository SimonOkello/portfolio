from django.shortcuts import render

# Create your views here.
from .models import (
    About,
    Skill,
    Service,
    Resume,
)


def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    resume = Resume.objects.all()

    context = {'about': about, 'skills': skills,
               'services': services, 'resume':resume}
    return render(request, 'home/index.html', context)
