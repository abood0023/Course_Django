# This file for can show my app in admin

from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) #Here you add your post in admin panel