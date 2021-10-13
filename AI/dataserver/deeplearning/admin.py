from django.contrib import admin

from .models import File, TrainedModel, Log


class FileAdmin(admin.ModelAdmin):
    list_display  = ['id', 'file', 'upload_at']

class TrainModelAdmin(admin.ModelAdmin):
    list_display  = ['version', 'file', 'result', 'matrix']

class LogAdmin(admin.ModelAdmin):
    list_display  = ['username', 'log', 'create_at']

admin.site.register(File, FileAdmin)
admin.site.register(TrainedModel, TrainModelAdmin)
admin.site.register(Log, LogAdmin)