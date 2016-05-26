from django.contrib import admin

from . import models


class AdAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted_at'
    list_filter = (
        'status',
    )
    search_fields = (
        'id',
        'title',
        'price',
    )
    list_display = (
        'id',
        'title',
        'status',
        'posted_at',
        'price',
    )


admin.site.register(models.Ad, AdAdmin)
