from django.contrib import admin
from .models import TimeCapsule, Photo, Sound, Document, Video, Comment, vote

@admin.register(TimeCapsule)
class TimeCapsuleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('creator', 'slug', 'created_date')


admin.site.register(Comment)            
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Sound)
admin.site.register(Document)



