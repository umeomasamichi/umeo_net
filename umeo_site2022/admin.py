from django.contrib import admin
#from .models import Message, Stock, Good

'''
class MessageAdmin(admin.ModelAdmin):
    fields = ['writer', 'body']
    list_display = ('writer', 'body', 'created_at')
    list_filter = ['writer']
    search_fields = ['writer']

class GoodAdmin(admin.ModelAdmin):
    fields = ['writer', 'body']
    list_display = ('writer', 'body', 'created_at')
    list_filter = ['writer']
    search_fields = ['writer']

class StockAdmin(admin.ModelAdmin):
    fields = ['value']
    list_display = ('value', 'created_at')

admin.site.register(Message, MessageAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Stock, StockAdmin)


'''