from django.conf.urls import patterns, include, url
from views import qiudai,bangdai,me,jia

urlpatterns = patterns('',
    # Examples:
    url(r'^$',bangdai,name='bangdai'),
    url(r'^qiudai/$',qiudai,name='qiudai'),
    url(r'^me/',me,name='me'),
    url(r'^jia/',jia,name='jia'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    #url(r'^admin/', include(admin.site.urls)),
    #(r'^accounts/', include('userena.urls')),
)