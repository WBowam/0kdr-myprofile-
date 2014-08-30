#-*- coding: UTF-8 -*- 
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
##for translate
from django.utils.translation import ugettext as _
#from userena.models import UserenaBaseProfile
##for img ,upload,resize
from stdimage import StdImageField
##for phone number at 'phone'
from django.core.validators import RegexValidator

class MyProfile(models.Model):
    ##
    check=models.BooleanField(default=False)
    mugshot=StdImageField(u'头像',upload_to='mugshot',blank=True,variations={'thumbnail': (160,160)})
    user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
    # user_state_CHOICES=((u'普通用户',u'普通用户'),(u'高级用户',u'高级用户'),(u'快递人',u'快递人'))
    # user_state=models.CharField(u'用户状态',max_length=20,choices=user_state_CHOICES,default=u'普通用户')
    # GENDER_CHOICES = ((1, _('Male')),(2, _('Female')),)
    # gender = models.PositiveSmallIntegerField(_('gender'),choices=GENDER_CHOICES,blank=True,null=True)
    date_joined=models.DateTimeField(u'注册时间',auto_now_add=True)
    student_number=models.CharField(u'学号',max_length=12,validators=[RegexValidator(regex='^\d{12}$', message='请输入正确的学号', code='Invalid number')])
    phone = models.CharField(u'电话',max_length=11,validators=[RegexValidator(regex='^\d{11}$', message='请输入正确的手机号', code='Invalid number')])
    one_card=StdImageField(u'一卡通',upload_to='onecard',blank=True,variations={'thumbnail': (340,216)}) # creates a thumbnail resized to maximum size to fit a 100x75 area
    #major=models.CharField(u'专业',max_length=100,blank=True)
    #address=models.ForeignKey(ReceiveAddress,verbose_name=u'收货地址',related_name='my_profile',help_text=u"目前只支持华电二校范围")
    #address=models.CharField(u'住址',max_length=100,blank=True)
    #phone=models.PositiveSmallIntegerField()
    #identity_card=models.CharField(u'身份证',max_length=100,blank=True)
   # student_number=models.CharField(u'学号',max_length=100,blank=True)
    #one_card=models.FileField(u'一卡通',null=True,blank=True,upload_to='onecard')


    def image_img(self):
        if self.one_card:
            return str('<img src="%s" />' % self.one_card.thumbnail.url)
        else:
            return u'上传一卡通'
    image_img.short_description = '一卡通'
    image_img.allow_tags = True
    def image_img2(self):
        if self.mugshot:
            return str('<img src="%s" />' % self.mugshot.thumbnail.url)
        else:
            return u'上传头像'
    image_img2.short_description = '头像'
    image_img2.allow_tags = True

    class Meta:
        verbose_name_plural=u'个人资料'
        #app_label=u'助学贷款'
        ordering=["-date_joined"]