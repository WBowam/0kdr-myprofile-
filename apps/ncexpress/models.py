#-*- coding: UTF-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
#from DjangoUeditor.models import UEditorField
import datetime
from django.core.validators import RegexValidator
# Create your models here.

class Express(models.Model):
	#got=models.BooleanField(u'被抢',default=False)
	expressed_by=models.ForeignKey(User,blank=True,verbose_name='帮带人',null=True,related_name='expressed_by')
	created_by = models.ForeignKey(User,default=1,verbose_name='创建人',related_name='created_by')
	b=((u'求带',u'求带'),(u'被抢',u'被抢'),(u'已送达',u'已送达'),(u'过期',u'过期'))
	express_status=models.CharField(u'快件状态',max_length=4,choices=b,default=u'求带')
	#f=((u'已代取',u'已代取'),(u'未代取',u'未代取'))
	#bought=models.CharField(u'代取情况',max_length=20,choices=f,default=u'未代取')
	a=((u'圆通',u'圆通'),(u'EMS',u'EMS'),(u'汇通',u'汇通'),(u'申通',u'申通'),(u'圆通',u'圆通'),(u'顺丰',u'顺丰'),(u'邮政小包',u'邮政小包'),(u'韵达',u'韵达'),(u'天天快递',u'天天快递'))
	express_company=models.CharField(u'快递公司',max_length=100,choices=a,default=u'申通')
	c=((u'服务中心',u'服务中心'),(u'北门',u'北门'),(u'南门',u'南门'))
	sourcePosition=models.CharField(u'取货地点',max_length=20,choices=c,default=u'服务中心')
	destinationPosition=models.CharField(u'送货地点',max_length=8)
	name=models.CharField(u'收件人名字',max_length=200)
	phone=models.CharField(u'收件人电话 ',max_length=11,validators=[RegexValidator(regex='^\d{11}$', message='请输入正确的手机号', code='Invalid number')])
	#upUser=models.ForeignKey(User)
	#now=datetime.datetime.now()
	#next=now+datetime.timedelta(hours=24)
	today=datetime.datetime.today()
	getDate=models.DateField(u'快件代取日期)',default=today)
	getTime=models.TimeField(u'快件代取时间',default=datetime.datetime.now)
	#getEndTime=models.DateTimeField(u'快件代取时间(结束)',default=next)
	#getBeginTime=models.DateTimeField(u'快件代取时间(开始)',help_text="请按格式输入:<em>YYYY-MM-DD HH-mm-SS</em>.",default=datetime.datetime.now)
	#getEndTime=models.DateTimeField(u'快件代取时间(结束)',default=next)
	h=((u'当日',u'当日'),(u'两天内',u'两天内'),(u'三天内',u'三天内'))
	deadLine=models.CharField(u'快件配送期限',max_length=20,choices=h,default=u'当日')	
	#postBeginTime=models.DateTimeField(u'快件送货时间(开始)')
	#postEndTime=models.DateTimeField(u'快件送货时间(结束)')
	#bianhao=models.CharField(max_length=30,unique=True)
	d=((u'小于1公斤重',u'小于1公斤重'),(u'小于5公斤重',u'小于5公斤重'),(u'小于10公斤重',u'小于10公斤重'),(u'小于50公斤重',u'小于50公斤重'))
	goodsWeight=models.CharField(u'快件重量',max_length=50,choices=d,default='小于1公斤重',blank=True)
	e=((u'信件',u'信件'),(u'书籍',u'书籍'),(u'衣服',u'衣服'),(u'鞋子',u'鞋子'),(u'其他',u'其他'))
	goodsVariety=models.CharField(u'快件种类',max_length=50,choices=e,default='信件',blank=True)
	message=models.TextField(u'备注',blank=True)
	upTime=models.DateTimeField(u'添加时间',auto_now=True)
	#,error_messages={'required': '别这么小气嘛，不给小费人家怎么给你送嘛'}
	tip=models.CharField(u'小费',max_length=20,default='2',help_text="默认单位“元”,普通快件推荐价格2元")
            
	def __unicode__(self):
		return "%s"%self.name

	# def __init__(self):
	# 	self.name='wo'

	class Meta:
		verbose_name_plural=u'快件'
		#ordering=['-upTime']



from xadmin.plugins.actions import BaseActionView
#from django.http import HttpResponse
#from django.shortcuts import render
from django.http import HttpResponseRedirect

class Songda(BaseActionView):

        # 这里需要填写三个属性
        action_name = "songda"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
        description = (u'标为送达') #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.

        model_perm = 'change'    #: 该 Action 所需权限

    # 而后实现 do_action 方法
        def do_action(self, queryset):
            # queryset 是包含了已经选择的数据的 queryset
            for obj in queryset:
                # obj 的操作
                obj.delivered='已送达'
                obj.save()
            # 返回 HttpResponse
            #return HttpResponseRedirect('/%s'%self.admin_site.name.app)
            return HttpResponseRedirect('/xadmin/ncexpress/express/')