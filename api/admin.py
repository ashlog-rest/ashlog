from django.contrib import admin
from api.models import Log, Project


class ModelAdmin(admin.ModelAdmin):
    exclude = ['id']


admin.site.register(Log, ModelAdmin)
admin.site.register(Project)
