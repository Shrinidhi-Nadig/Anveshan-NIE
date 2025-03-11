from django.contrib import admin
from members.models import Members

class MembersAdmin(admin.ModelAdmin):
    list_display=('member_image','member_name','member_linkedin','member_git')

admin.site.register(Members,MembersAdmin)