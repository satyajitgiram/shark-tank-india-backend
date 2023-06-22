from django.contrib import admin
from .models import Entrepreneur, Pitch, Shark
# Register your models here.
admin.site.register(Shark)
admin.site.register(Entrepreneur)
admin.site.register(Pitch)