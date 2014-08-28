#-*- coding: UTF-8 -*- 
from django.shortcuts import render
from models import Express
from django.contrib.auth.decorators import login_required
from forms import ExpressForm
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
# Create your views here.

@login_required
def create_express(request):
    form = ExpressForm(request.POST or None)
    if form.is_valid():
    	
        express=form.save(commit=False)
        express.created_by=request.user
        express.save()
    	form = ExpressForm()

    	#return HttpResponseRedirect(reverse('apps.ncexpress.views.my_express',args=['all']))
        messages.success(request, "Your data has been saved!")
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect("/express/listexpress/")
    return render(request,'ncexpress/create_express.html',{'form':form})



def list_express(request):
  
    express=Express.objects.filter(express_status=u'求带')    
    return render(request,'index/bangdai.html',{'express':express})




@login_required
def my_express(request,which='all'):
	if which=='all':
		my_express=Express.objects.filter(Q(created_by=request.user) | Q(expressed_by=request.user))
	elif which=='created':
		my_express=Express.objects.filter(created_by=request.user)
	elif which=='expressed':
		my_express=Express.objects.filter(expressed_by=request.user)
	else:
		pass
	return render(request,'ncexpress/my_express.html',{'my_express':my_express})


@login_required
def edit_express(request,id):

    express_instance = Express.objects.get(id=id)

    form = ExpressForm(request.POST or None, instance = express_instance)

    if form.is_valid():
        form.save()
        messages.success(request, "Your data has been saved!")
        #return HttpResponseRedirect("/express/myexpress/")
        return HttpResponseRedirect(reverse('apps.ncexpress.views.my_express',args=['all']))
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'ncexpress/edit_express.html',{'form':form})
@login_required
def cancle_express(request,id):
    express = Express.objects.get(id=id)
    express.express_status=u'过期'
    express.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def help_express(request,id):
    express = Express.objects.get(id=id)
    express.express_status=u'被抢'
    express.expressed_by=request.user
    express.save()
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect('/')
