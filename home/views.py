from django.shortcuts import render

# Create your views here.
from .models import (
    About,
    Skill,
    Service,
    Resume,
    Portfolio,
)


def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    resume = Resume.objects.all()
    portfolio = Portfolio.objects.all()
    common_tags = Portfolio.tags.most_common()

    context = {'about': about, 'skills': skills,
               'services': services, 'resume': resume,
               'portfolio': portfolio, 'common_tags':common_tags,}
    return render(request, 'home/index.html', context)
