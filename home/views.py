from django.shortcuts import render

# Create your views here.
from .models import (
    About,
    Skill,
)


def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()

    context = {'about': about, 'skills': skills}
    return render(request, 'home/index.html', context)
