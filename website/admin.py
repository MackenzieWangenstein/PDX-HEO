from django.contrib import admin
from .models import Organization
from .models import ServiceType
from .models import Service


# Register your models here.
class ServiceInline(admin.TabularInline):
  model = Service
  extra = 1


class OrganizationAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Organization Details', {'fields': ['name', 'description', 'address', 'hours_open', 'hours_close']}),
    ('Contact Details', {'fields': ['phone', 'website', 'email']}),
  ]
  inlines = [ServiceInline]
  list_display = ('name', 'address', 'pub_date', 'updated_date')
  list_filter = ['pub_date', 'updated_date']
  search_fields = ['name']


class ServiceAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Organization', {'fields': ['organization']}),
    ('Service Type', {'fields': ['type']}),
    ('Service Details', {'fields': ['name', 'description', 'address', 'hours_open', 'hours_close']}),
    ('Contact Details', {'fields': ['phone', 'website', 'email']}),
  ]
  list_display = ('name', 'organization', 'type', 'address', 'pub_date', 'updated_date')
  list_filter = ['pub_date', 'updated_date', 'type']
  search_fields = ['name']


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ServiceType)
admin.site.register(Service, ServiceAdmin)
