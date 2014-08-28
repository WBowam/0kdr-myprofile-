#-*- coding: UTF-8 -*- 
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from apps.ncexpress.forms import ExpressForm
from apps.ncexpress.models import Express


@login_required
def bangdai(request):
	bangdai_list=Express.objects.filter(express_status=u'求带').order_by('-upTime')[0:10]
	return render(request,'index/bangdai.html',{'bangdai_list':bangdai_list})

@login_required
def qiudai(request):
####create_express####create_express####create_express####create_express
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
####list_express####list_express####list_express####list_express

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