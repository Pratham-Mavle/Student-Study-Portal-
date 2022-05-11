from django.contrib import admin

from dashboard.views import youtube
from . models import *
# Register your models here.

admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)
#admin.site.register(youtube)