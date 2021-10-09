from django.urls import path

from .views import (
    registerView,
)

app_name = 'accounts'
urlpatterns = [
    path('signup/', registerView, name='register-view'),
]
