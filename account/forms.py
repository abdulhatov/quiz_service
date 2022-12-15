from django import forms
from django.contrib.auth.models import User

class AccountRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'special', 'size': 45})
        self.fields['last_name'].widget.attrs.update({'class': 'special', 'size': 45})
        self.fields['email'].widget.attrs.update({'class': 'special', 'size': 45})
        self.fields['username'].widget.attrs.update({'class': 'special', 'size': 45})
        self.fields['password'].widget.attrs.update(size='45')
        self.fields['password2'].widget.attrs.update(size='45')

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class AccountLoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'special', 'size': 45})
        self.fields['password'].widget.attrs.update({'class': 'special', 'size': 45})

