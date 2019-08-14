from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from rest_framework.authtoken.admin import TokenAdmin
# from rest_framework.authtoken.models import Token

from .models import (
    User,
    Dashboard,
    Inquiry,
    Prepaidplans,
    Dongleplans,
    Profile,
    Recharge,
    Feedback,
    Preform,
    Postform,
    Dongleform
)
# Register your models here.
admin.site.register(Profile, UserAdmin)
admin.site.register(Dashboard)
admin.site.register(Recharge)
admin.site.register(Dongleplans)
admin.site.register(Prepaidplans)
admin.site.register(Inquiry)
admin.site.register(Feedback)
admin.site.register(Preform)
admin.site.register(Postform)
admin.site.register(Dongleform)
# admin.site.register(TokenAdmin)
# TokenAdmin.raw_id_fields = ['user']
