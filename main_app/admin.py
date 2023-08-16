from django.contrib import admin
from .models import Train, Route, Destination, RouteDestinationSchedule, SchedulingInfo

# Register your models here.

admin.site.register(Train)
admin.site.register(RouteDestinationSchedule)
admin.site.register(SchedulingInfo)
admin.site.register(Route)
admin.site.register(Destination)