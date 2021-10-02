from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocSignupForm
from django.contrib.auth.models import Group


class BasicSignupForm(SignupForm):
    
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user

class SocialSignupForm(SocSignupForm):

    def save(self, request):
        user = super(SocialSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user