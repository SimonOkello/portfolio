from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your views here.

def registerView(request):
    form = UserCreationForm()
    context ={'form':form}
    return render(request, 'accounts/register.html', context)