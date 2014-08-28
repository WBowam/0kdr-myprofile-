from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from userena.utils import get_profile_model, get_user_model
from models import Express

class ExpressForm(ModelForm):
    

    class Meta:
        model = Express
        #model= MyProfile
        exclude = ['got','tip','created_by','expressed_by','express_status','getTime','getDate']


    # def save(self,request,commit=True, *args, **kwargs):

    #     print 'request.user.id:',request.user.id

    #     instance = super(ExpressForm, self).save(commit=False)
    #     if commit:
    #         instance.save(request=request)
    #     if request:
    #         instance.modifier = request.user
    #         instance.save(request=request)
    #     return instance