from django.conf.urls import patterns, include, url
from views import create_express,my_express,list_express,edit_express,cancle_express,help_express


urlpatterns = patterns('',
    # Examples:
    url(r'^create/$', create_express,name='create_express'),
    url(r'^myexpress/(?P<which>[^/]+)/$', my_express,name='my_express'),
    url(r'^listexpress/$', list_express,name='list_express'),
    url(r'edit/(?P<id>[^/]+)/$', edit_express,name='edit_express'),
    url(r'cancle/(?P<id>[^/]+)/$', cancle_express,name='cancle_express'),
    url(r'help/(?P<id>[^/]+)/$', help_express,name='help_express'),
    #url(r'^list/(?P<name>[^/]+)/$',list, name='list'),
    #url(r'^create$', include('apps.index.urls')),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    #url(r'^admin/', include(admin.site.urls)),
    #(r'^accounts/(?P<username>[^/]+)/edit/$','userena.views.profile_edit',{'edit_profile_form':MyEditProfileForm}),
    #(r'^accounts/', include('userena.urls')),
)