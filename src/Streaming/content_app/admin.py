from django.contrib import admin

from content_app.models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public')
    list_filter = ('content_type', 'is_public')
    search_fields = ('title', 'description')
    ordering = ['-upload_date']

# Register your models here.
admin.site.register(Content, ContentAdmin)


