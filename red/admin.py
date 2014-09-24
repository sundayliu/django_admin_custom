from django.contrib import admin

# Register your models here.
from red.models import Document,Comment

class DocumentAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Document, DocumentAdmin)
admin.site.register(Comment,CommentAdmin)