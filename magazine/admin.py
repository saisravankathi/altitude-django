from django.contrib import admin

# Register your models here.
from .models import Publisher, Story, Content

admin.site.register(Publisher)
admin.site.register(Story)
admin.site.register(Content)
