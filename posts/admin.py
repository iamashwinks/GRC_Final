from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Articles)
admin.site.register(Type)
admin.site.register(Comment)