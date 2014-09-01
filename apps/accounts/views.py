#-*- coding: UTF-8 -*- 
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from models import MyProfile
from forms import MyProfileForm,MyUserCreationForm,MyLoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
# Create your views here.

# def create(request):
# 	form = MyProfileForm(request.POST or None)
# 	if form.is_valid():
# 		profile=form.save(commit=False)
# 		profile.user=request.user
# 		profile.save()
# 		form = MyProfileForm()
#         return HttpResponseRedirect("/")
# 	return render(request,'accounts/profile_create.html',{'form':form})

@login_required
def create(request):
	try:
		user_detail=MyProfile.objects.get(user=request.user)
	except Exception, e:
		if request.method=='POST':
			form=MyProfileForm(request.POST,request.FILES)
			if form.is_valid():
				#mugshot=form.cleaned_data['mugshot']
				#onecard=request.FIELS
				profile=form.save(commit=False)
				profile.user=request.user
				profile.mugshot=request.FILES['mugshot']
				profile.one_card=request.FILES['one_card']
				#profile.mugshot=mugshot
				profile.save()
				#form = MyProfileForm()
				return HttpResponseRedirect("/accounts/detail/")
			else:
				return render(request,'accounts/profile_create.html',{'form':form})	
		else:
			form=MyProfileForm()
			return render(request,'accounts/profile_create.html',{'form':form})
	return HttpResponseRedirect("/accounts/detail/")

def detail(request):
	referer=request.META.get('HTTP_REFERER', '/')
	try:
		user_detail=MyProfile.objects.get(user=request.user)
		title=u'个人资料'
		return render(request,'accounts/profile_detail.html',{'user_detail':user_detail,'referer':referer,'title':title})
	except Exception, e:
		return HttpResponseRedirect('/accounts/create/')


# def detail(request):
# 	user_detail=get_object_or_404(MyProfile,user=request.user)
# 	return render(request,'accounts/profile_detail.html',{'user_detail':user_detail})


# def edit(request):
# 	try:
# 		user_profile_instance=MyProfile.objects.get(user=request.user)
# 		form=MyProfileForm(request.POST or None,instance=user_profile_instance)
# 		if form.is_valid():
# 			profile=form.save(commit=True)
# 			profile.user=request.user
# 			profile.save()
# 			#messages.success(request, "Your data has been saved!")
# 			#return HttpResponseRedirect("/express/myexpress/")
# 			return HttpResponseRedirect(reverse('apps.accounts.views.detail'))
# 			#return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
# 		return render(request,'accounts/profile_edit.html',{'form':form})
# 	except Exception, e:
# 		return HttpResponseRedirect(reverse('apps.accounts.views.create'))


def edit(request):
	if request.method=='POST':
		form=MyProfileForm(request.POST or None)
		if form.is_valid():
			profile=form.save(commit=True)
			profile.user=request.user
			profile.save()
			#messages.success(request, "Your data has been saved!")
			#return HttpResponseRedirect("/express/myexpress/")
			return render(request,'accounts/profile_detail.html',{'form':profile})
		return render(request,'accounts/edit.html',{'form':form})
	else:
		try:
			user_profile_instance=MyProfile.objects.get(user=request.user)
			form=MyProfileForm(instance=user_profile_instance)
			return render(request,'accounts/edit.html',{'form':form})
		except Exception, e:
			return HttpResponseRedirect(reverse('apps.accounts.views.create'))

def login_success(request):
	return render(request,'accounts/login_success.html')


# def login_view(request):  
#     #表单提交过来的数据  
#     if request.user.is_authenticated():
#         return  HttpResponseRedirect('/')
#     if request.method == 'POST':  
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)  
#         if user is not None:  
#             if user.is_active:
#                     login(request,user)  
#                     return HttpResponseRedirect('/')  
#             else:  
#             	message=u'用户没有激活!请登录邮箱激活...或联系客服'
#                 return render_to_response('accounts/login.html',{'message':message})
#         else:  
# 			message=u'用户名或者密码错误！'
# 			return render_to_response('accounts/login.html',{'message':message})
#     else:
#         return render_to_response('accounts/login.html')






def login_view(request):
	if request.user.is_authenticated():
		return  HttpResponseRedirect('/index/bangdai')
	form = MyLoginForm()
	error=''
	if request.method == 'POST':
		form = MyLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None and user.is_active:
				login(request, user)

				return HttpResponseRedirect("/index/bangdai/")

			else :
				form = MyLoginForm(request.POST)
				error = "用户名或密码错误"

	return render_to_response("accounts/login.html",
    {'form': form,'error':error,},
    context_instance=RequestContext(request)
    )



def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/accounts/login")

def register(request):
    
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/accounts/login/")
	else:
		form = MyUserCreationForm()
	return render_to_response("accounts/register.html",
	{'form': form,},
	context_instance=RequestContext(request)
	)


def password_reset(request):
	if request.method=='POST':
		try:
			user=User.objects.get(id=request.user.id)
		except Exception, e:
			return HttpResponseRedirect("/accounts/login/")
		password_current=request.POST['password_current']
		check=authenticate(username=user.username,password=password_current)
		if check :
			password_one=request.POST['password_one']
			password_two=request.POST['password_two']
			if password_one == password_two :
				user.set_password(password_one)
				user.save()
				#logout(request)
				return HttpResponseRedirect("/index/me/")
				#return render(request,'accounts/password_reset_success.html')
			else :
				error=u"新密码两次不一致"
				return render(request,'accounts/password_reset.html',{ 'error':error })
		else:
			error="目前的密码输入错误"
			return render(request,'accounts/password_reset.html',{ 'error':error,'error0':error0 })
	else:
		return render(request,'accounts/password_reset.html')