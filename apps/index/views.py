#-*- coding: UTF-8 -*- 
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from django.db.models import Q
from django.utils import timezone
# Create your views here.
from apps.ncexpress.forms import ExpressForm
from apps.ncexpress.models import Express


@login_required
def bangdai(request,source=''):
	#now=datetime.datetime.now()
	now = timezone.now()
	upTime = now - datetime.timedelta(hours=48, minutes=59, seconds=59)
	bangdai_list = Express.objects.filter(upTime__gt=upTime).filter(express_status=u'求带').order_by('-upTime')[0:10]
	#bangdai_list=Express.objects.filter(express_status=u'求带').order_by('-upTime')[0:10]
	if source=='':
		bangdai_list = Express.objects.filter(Q(getDate__gt=upTime) & Q(express_status=u'求带')).order_by('-upTime')[0:10]
	elif source == 'fwzx':
		bangdai_list = Express.objects.filter(Q(getDate__gt=upTime) & Q(express_status=u'求带') & Q(sourcePosition ="服务中心")).order_by('-upTime')[0:10]
	elif source == 'nm':
		bangdai_list = Express.objects.filter(Q(getDate__gt=upTime) & Q(express_status=u'求带') & Q(sourcePosition ="南门")).order_by('-upTime')[0:10]
	elif source == 'bm':
		bangdai_list = Express.objects.filter(Q(getDate__gt=upTime) & Q(express_status=u'求带') & Q(sourcePosition ="北门")).order_by('-upTime')[0:10]
	return render(request,'index/bangdai.html',{'bangdai_list':bangdai_list})



def home(request):
	return render(request,'index.html')



@login_required
def qiudai(request):
	qiudai_list = ExpressForm(request.POST or None)
	if qiudai_list.is_valid():
		express1=qiudai_list.save(commit=False)
		express1.getDate=request.POST['getdate']
		express1.getTime=request.POST['gettime']
		express1.tip=request.POST['tip']
		express1.created_by=request.user
		express1.save()
		qiudai_list = ExpressForm()
		#return HttpResponseRedirect(reverse('apps.ncexpress.views.my_express',args=['all']))
		#messages.success(request, "Your data has been saved!")
		#return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		return HttpResponseRedirect("/")
	return render(request,'index/qiudai.html',{'qiudai_list':qiudai_list})




def me(request):
	
	return render(request,'index/me.html')


import datetime

@login_required
def jia(request):
	i=1
	while i<100:
		
		try:
			e=Express(name="sdfhd",phone="12345678987")
			e.save()
			message="yes"

		except Exception, e:
			message="no"
		i=i+1

	return render(request,'userena/signin_success.html',{'message':message,'i':i})
