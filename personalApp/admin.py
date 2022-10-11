from django.contrib import admin

from .models import (
    Department,
    Personal
)

# Register your models here.
admin.site.register(Department)
admin.site.register(Personal)