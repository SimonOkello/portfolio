from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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
    skill_tags = Skill.skill_tags.most_common()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        subject = f'{name}({email})'
        if name and email and message:
            send_mail(subject, message, email,
                      ['simonokello93@gmail.com'], fail_silently=False)
            messages.success(request, 'Email sent!')
        else:
            messages.error(request, 'Fill all the fields!')

    context = {'about': about, 'skills': skills,
               'services': services, 'resume': resume,
               'portfolio': portfolio, 'common_tags': common_tags,
               'skill_tags': skill_tags}
    return render(request, 'home/index.html', context)
