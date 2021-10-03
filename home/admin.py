from django.contrib import admin

# Register your models here.
from .models import (
    About,
    Skill,
    Service,
)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Service)
