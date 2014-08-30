from django.conf.urls import patterns, include, url

from apps.accounts.forms import *
import xadmin
xadmin.autodiscover()

from django.contrib import admin
admin.autodiscover()
from apps.index.views import home



urlpatterns = patterns('',
    # Examples:
    
    url(r'^express/', include('apps.ncexpress.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^admin/', include(admin.site.urls)),
    #(r'^accounts/(?P<username>[^/]+)/edit/$','userena.views.profile_edit',{'edit_profile_form':MyProfileForm}),
    (r'^accounts/', include('apps.accounts.urls')),
    url(r'^index/', include('apps.index.urls')),
    url(r'^$',home,name='home'),
)

##added by Tulpar,20140818
from django.conf import settings

urlpatterns += patterns('',
    url(r"^media/(?P<path>.*)$","django.views.static.serve",{"document_root": settings.MEDIA_ROOT,}),
)


##added by Tulpar,20140818
##from django.conf import settings
urlpatterns += patterns('',
    url(r"^static/(?P<path>.*)$","django.views.static.serve",{"document_root": settings.STATIC_ROOT,}),
    )

# ###Django-Debug-toolbar Begin

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
# ###Django-Debug-toolbar End