from django.contrib import admin

from . import models

# Adds Checklist and Category models to the Admin
admin.site.register(models.Checklist)
admin.site.register(models.Category)
