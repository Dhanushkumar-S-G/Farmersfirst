from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(models.Product)

class ViewAdmin(ImportExportModelAdmin):
    pass
admin.site.register(models.Cart)