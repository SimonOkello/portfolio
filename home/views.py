from django.shortcuts import render

# Create your views here.
from about.models import About

def index(request):
    about = About.objects.all()

    context = {'about':about}
    return render(request, 'home/index.html', context)
