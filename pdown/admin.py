from django.contrib import admin
from .models import Post
from pagedown.widgets import AdminPagedownWidget
from django.db import models


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
