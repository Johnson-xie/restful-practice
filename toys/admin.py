from django.contrib import admin
from .models import Toy


@admin.register(Toy)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')

