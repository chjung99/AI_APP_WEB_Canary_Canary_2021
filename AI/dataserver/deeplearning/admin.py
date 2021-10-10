from django.contrib import admin

from .models import File, TrainedModel


class FileAdmin(admin.ModelAdmin):
    list_display  = ['id', 'file', 'upload_at']

class TrainModelAdmin(admin.ModelAdmin):
    list_display  = ['version', 'file', 'result']

admin.site.register(File, FileAdmin)
admin.site.register(TrainedModel, TrainModelAdmin)