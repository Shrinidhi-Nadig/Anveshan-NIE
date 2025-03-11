from django.contrib import admin
from Subscribers.models import Subscriber
# Register your models here.
class SubscribeAdmin(admin.ModelAdmin):
    list_display=('subscribers_name','subscribers_email')

admin.site.register(Subscriber,SubscribeAdmin)