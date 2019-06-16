from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class FormForLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'un','type':'text','align':'center','placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'pass','type':'password','align':'center','placeholder':'Password'
    }))

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect!')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
        return super(FormForLogin,self).clean(*args,**kwargs)


class FormForSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','username','password']

        widgets = {
            'email':forms.EmailInput(attrs={'class':'un','type':'email','align':'center','placeholder':'Email'}),
            'username':forms.TextInput(attrs={'class':'un','type':'text','align':'center','placeholder':'Username'}),
            'password':forms.PasswordInput(attrs={'class':'pass','type':'password','align':'center','placeholder':'Password'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email = email)
        if email_qs.exists():
            raise forms.ValidationError('This email is already exist')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username = username)
        if username_qs.exists():
            raise forms.ValidationError('This username is already exist')
        return username


class FormForChangePassword(forms.ModelForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'pass','type':'password','align':'center','placeholder':'New password'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'pass','type':'password','align':'center','placeholder':'Confirm new password'
    }))
    class Meta:
        model = User
        fields = ['password','new_password1','new_password2']

        widgets = {
            'password':forms.PasswordInput(attrs={'class':'pass','type':'password','align':'center','placeholder':'Old Password'}),
        }

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user')
         super(FormForChangePassword, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not self.user.check_password(password):
            raise forms.ValidationError("Old password is incorrect")
        return password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords isn't the same")
        return password2
