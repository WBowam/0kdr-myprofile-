from django.conf.urls import patterns, include, url
from views import detail,edit,create,login_view,logout_view,login_success,register,password_reset


urlpatterns = patterns('',
    # Examples:
    #url(r'edit/(?P<id>[^/]+)/$', edit_express,name='edit_express'),
    #url(r'detail/(?P<id>[^/]+)/$', cancle_express,name='cancle_express'),
    #url(r'help/(?P<id>[^/]+)/$', help_express,name='help_express'),
    #url(r'^list/(?P<name>[^/]+)/$',list, name='list'),
    #url(r'^create$', include('apps.index.urls')),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$',register,name="register"),
    url(r'^login/$',login_view,name="login_view"),
    #url(r'^loginsuccess/$',login_success,name="login_success"),
    url(r'^logout/$',logout_view,name="logout_view"),
    url(r'^create/$',create,name="create"),
    url(r'^detail/$',detail,name="profile_detail"),
    url(r'^edit/$',edit,name="profile_edit"),
    url(r'^passwordreset/$',password_reset,name="password_reset"),
    #(r'^accounts/', include('userena.urls')),
)