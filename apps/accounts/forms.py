#coding=utf-8
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
#from userena.utils import get_profile_model, get_user_model
from models import MyProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyProfileForm(ModelForm):
    

    class Meta:
        #model = get_profile_model()
        model= MyProfile
        exclude = ['user','check']

    # def save(self, force_insert=False, force_update=False, commit=True):
    #     profile = super(MyProfileForm, self).save(commit=commit)
    #     # Save first and last name
    #     user = profile.user
    #     #user.first_name = self.cleaned_data['first_name']
    #     #user.last_name = self.cleaned_data['last_name']
    #     user.save()

    #     return profile

class MyUserCreationForm(UserCreationForm): 
    username = forms.RegexField(label=(u"用户名"), max_length=30,
                regex=r'^[\w.@+-]+$',
                widget=forms.TextInput(attrs={'placeholder': '只能用字母、数字和字符', }),

                #help_text=("只能用字母、数字和字符."), #use placeholder to replace it
                error_messages={
                    'invalid': ("只能用字母、数字和字符")})     
    class Meta:
             model = User
             fields = ("username",)




class MyLoginForm(forms.Form): 
    username = forms.CharField(required=True,
                                label='用户名',
                                widget=forms.TextInput(attrs={'placeholder': '用户名', })
                                )
    password = forms.CharField(required=True,label='密码',widget=forms.PasswordInput(
                                                    attrs={'placeholder': '密码', }))