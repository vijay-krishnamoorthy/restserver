from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# from django.contrib.auth.viewsets import RegisterViewSet
# from rest_framework.views import RegisterView
from .models import (
    User,
    Profile,
    Dashboard,
    Recharge,
    Inquiry,
    Dongleplans,
    Prepaidplans,
    Feedback,
    Preform,
    Postform,
    Dongleform,
)
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    RechargeSerializer,
    InquirySerializer,
    PrepaidSerializer,
    DongleSerializer,
    FeedbackSerializer,
    PreformSerializer,
    PostformSerializer,
    DongleformSerializer
)



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class UserViewSet(ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=UserSerializer

# class UserRegisterView(RegisterView):
#     model=User
#     queryset=User.objects.all()

class ProfileViewSet(ModelViewSet):
    queryset=Dashboard.objects.all()
    serializer_class=ProfileSerializer

# class DashboardViewSet(ModelViewSet):
#     queryset=Dashboard.objects.all()
#     serializer_class=DashboardSerializer

class InquiryViewSet(ModelViewSet):
    queryset=Inquiry.objects.all()
    serializer_class=InquirySerializer

class DongleViewSet(ModelViewSet):
    queryset=Dongleplans.objects.all()
    serializer_class=DongleSerializer

class PrepaidViewSet(ModelViewSet):
    queryset=Prepaidplans.objects.all()
    serializer_class=PrepaidSerializer

class RechargeViewSet(ModelViewSet):
    queryset=Recharge.objects.all()
    serializer_class=RechargeSerializer

class FeedbackViewSet(ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
class PreformViewSet(ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Preform.objects.all()
    serializer_class=PreformSerializer

class PostformViewSet(ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Postform.objects.all()
    serializer_class=PostformSerializer

class DongleformViewSet(ModelViewSet): #viewset methods:list,create,retrieve,update,partial_update,destroy
    queryset=Dongleform.objects.all()
    serializer_class=DongleformSerializer