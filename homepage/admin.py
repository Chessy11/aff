from django.contrib import admin
from .models import Homepage


class HomepageAdmin(admin.ModelAdmin):
    list_display = ('video',)


admin.site.register(Homepage)
