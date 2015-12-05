from django.contrib import admin

from .models import Project, ProjectImage

class ImageInline(admin.TabularInline):
    model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['project_name', 'short_description', 'long_description', 'mainimage', 'link']}),
        ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),]
    inlines = [ImageInline]
    list_display = ('project_name', 'short_description', 'long_description')
    list_filter = ['pub_date']
    search_fields = ['project_name']

admin.site.register(Project, ProjectAdmin)
