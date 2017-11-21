from django.contrib import admin

from .models import JobAPI, JobPost


class APIAdmin(admin.ModelAdmin):
    list_display = ('search_must_contain', 'search_at_least_one', 'search_cant_contain',
                    'city', 'state', 'url_updated')
    ordering = ('url_updated', 'state', 'city',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'city', 'state', 'date')
    ordering = ('date', 'state', 'city', 'company')


admin.site.register(JobAPI, APIAdmin)
admin.site.register(JobPost, PostAdmin)
