from rest_framework.serializers import ModelSerializer
from .models import (
    User,
    Profile,
    Inquiry,
    Dongleplans,
    Recharge,
    Prepaidplans,
    Dashboard,
    Feedback,
    Preform,
    Postform,
    Dongleform,
)

class UserSerializer(ModelSerializer):
    class Meta:
        model=Profile
        fields=('id','username','email','password','phone')
        lookup_field='phone'

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
         fields=('id','mobile','amount','rdate','pid')

class DongleSerializer(ModelSerializer):
    class Meta:
        model=Dongleplans
        fields=('id','planname','data','validity','price')

class FeedbackSerializer(ModelSerializer):
    class Meta:
         model=Feedback
         fields=('id','fname','femail','fsubject','fmessage')
        
        
class PreformSerializer(ModelSerializer):
    class Meta:
            model=Preform
            fields=('id','name','email','mobile','address','city','pincode','num')
        
class PostformSerializer(ModelSerializer):
    class Meta:
             model=Postform
             fields=('id','name','email','mobile','address','city','pincode','num')
        
class DongleformSerializer(ModelSerializer):
    class Meta:
             model=Dongleform
             fields=('id','name','email','mobile','address','city','pincode')
