from django.contrib import admin

from user.models import Profile, CustomUser, Role

admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(CustomUser)
