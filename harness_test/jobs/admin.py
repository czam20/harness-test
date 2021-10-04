from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Job Admin"""
        
    list_display = ('pk', 'title')
    list_display_links = ('pk', 'title')

    search_fields = (
        'title',
        'skills'
    )

    list_filter = (
        'title',
    )

    fieldsets = (
        ('Job', {
            'fields': (('title', 'skills', 'description'),),
        }),
    )
    
    readonly_fields = ('id',)

