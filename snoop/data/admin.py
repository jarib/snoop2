from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from . import models


def blob_link(blob_pk):
    url = reverse('admin:data_blob_change', args=[blob_pk])
    return mark_safe(f'<a href="{url}">{blob_pk[:10]}...{blob_pk[-4:]}</a>')


class FileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'size', 'mime_type', 'blob_link']
    search_fields = [
        'name',
        'blob__sha3_256',
        'blob__sha256',
        'blob__sha1',
        'blob__md5',
        'blob__magic',
        'blob__mime_type',
        'blob__mime_encoding',
    ]

    def mime_type(self, obj):
        return obj.blob.mime_type

    def blob_link(self, obj):
        return blob_link(obj.blob.pk)

    blob_link.short_description = 'blob'


class BlobAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'mime_type', 'mime_encoding']
    list_filter = ['mime_type']
    search_fields = ['sha3_256', 'sha256', 'sha1', 'md5',
                     'magic', 'mime_type', 'mime_encoding']
    readonly_fields = ['sha3_256', 'sha256', 'sha1', 'md5']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'func', 'args', 'status']
    list_filter = ['func', 'status']
    search_fields = ['pk', 'func', 'args']


class DigestAdmin(admin.ModelAdmin):
    list_display = ['pk', 'collection', 'blob__mime_type', 'blob_link',
                    'result_link', 'date_modified']
    list_filter = ['collection__name', 'blob__mime_type']
    search_fields = ['pk', 'collection__pk', 'blob__pk', 'result__pk']

    def blob__mime_type(self, obj):
        return obj.blob.mime_type

    def blob_link(self, obj):
        return blob_link(obj.blob.pk)

    def result_link(self, obj):
        return blob_link(obj.result.pk)


admin.site.register(models.Collection)
admin.site.register(models.Directory)
admin.site.register(models.File, FileAdmin)
admin.site.register(models.Blob, BlobAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.TaskDependency)
admin.site.register(models.Digest, DigestAdmin)
