from django.contrib import admin

# Register your models here.
from .models import (
    About,
    Skill,
    Service,
    Resume,
    Portfolio,
)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Resume)
admin.site.register(Portfolio)
