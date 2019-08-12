from rest_framework.serializers import ModelSerializer
from .models import User, Profile,Inquiry,Dongleplans,Recharge,Prepaidplans,Dashboard

class UserSerializer(ModelSerializer):
    class Meta:
        model=Profile
        fields=('id','username','email','password','phone')
class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Dashboard
        fields='__all__'

class PrepaidSerializer(ModelSerializer):
    class Meta:
        model=Prepaidplans
        fields=('id','planname','planprice','planduration','plandes')
class InquirySerializer(ModelSerializer):
    class Meta:
         model=Inquiry
         fields=('id','name','phone','email','message')
class RechargeSerializer(ModelSerializer):
    class Meta:
         model=Recharge
         fields=('id','mobile','amount','rdate')

class DongleSerializer(ModelSerializer):
    class Meta:
        model=Dongleplans
        fields=('id','planname','data','validity','price')
