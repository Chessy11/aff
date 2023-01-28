from django.contrib import admin

# Register your models here.
from import_export.admin import ExportActionMixin
from .models import Contact

class ContactAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'experience_in_crypto', 'if_decided_to_invest')
    list_filter = ('name', 'email', 'phone', 'experience_in_crypto', 'if_decided_to_invest')
    search_fields = ('name', 'email', 'phone', 'experience_in_crypto', 'if_decided_to_invest')
    list_per_page = 25
    

admin.site.register(Contact, ContactAdmin)
