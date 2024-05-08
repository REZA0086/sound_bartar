from django import forms
from account.models import CustomerUser


class LoginForm(forms.ModelForm):
    user_phone = forms.CharField(max_length=11)
    class Meta:
        model = CustomerUser
        fields = ['password', 'active_code']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['user_phone', 'name', 'family', 'password']


class RecoveryPassForm(forms.Form):
    user_phone = forms.CharField(max_length=11)


class ActiveCodeForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['active_code']


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['password']
