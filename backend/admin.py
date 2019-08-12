from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Dashboard, Inquiry, Prepaidplans, Dongleplans, Profile,Recharge
# Register your models here.
admin.site.register(Profile, UserAdmin)
admin.site.register(Dashboard)
admin.site.register(Recharge)
admin.site.register(Dongleplans)
admin.site.register(Prepaidplans)
admin.site.register(Inquiry)