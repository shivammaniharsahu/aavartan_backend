from django.contrib import admin
from Events.models import Event
from registration.models import User


# Register your models here.
admin.site.register(User)
admin.site.register(Event)