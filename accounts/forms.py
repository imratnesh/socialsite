from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    # gender = forms.RadioSelect(choices=('M', 'F'))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def cleanpassword2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password did not match')
        return cd['password']
