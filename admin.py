from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Trip)
admin.site.register(Booking)
admin.site.register(Location)