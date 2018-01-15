from django.contrib import admin
from .models import BusOrganisation, Route, Bus, Schedule

# Register your models here.
admin.site.register(BusOrganisation)
admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Schedule)

