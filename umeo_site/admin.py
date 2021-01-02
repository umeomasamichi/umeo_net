from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    fields = ['writer', 'body']
    list_display = ('writer', 'body', 'created_at')
    list_filter = ['writer']
    search_fields = ['writer']

admin.site.register(Message, MessageAdmin)
