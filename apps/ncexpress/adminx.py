#-*- coding: UTF-8 -*- 
#from django.contrib import admin
import xadmin

from models import Express,Songda


from xadmin import views
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)

class ExpressAdmin(object):
	#search_fields=('name','category','content')
	#prepopulated_fields = { 'message': ['name'] }##learned at  http://www.b-list.org/weblog/2008/dec/24/admin/
	#exclude = ('created_by',)
	actions = [Songda, ]
	list_display = ('name',)
	list_display_links = ('name',)
	ordering = ("-upTime",)
	list_filter=('sourcePosition','upTime','destinationPosition')#该属性指定可以过滤的列的名字, 系统会自动生成搜索器
	search_fields=('destinationPosition','sourcePosition','name','delivered')#属性指定可以通过搜索框搜索的数据列的名字, 搜索框搜索使用的是模糊查找的方式, 一般用来搜素名字等字符串字段
	list_export = ('xls', 'xml', 'json')#该插件在数据列表页面提供了数据导出功能, 可以导出 Excel, CSV, XML, json 格式.
	# 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
	refresh_times = (3, 5,500)
	#list_editable = ('delivered')
	show_detail_fields = ['message',]#该插件可以在列表页中显示相关字段的详细信息, 使用 Ajax 在列表页中显示.


	# def save_models(self):
	# 	self.new_obj.created_by=self.request.user
	# 	self.new_obj.save()

xadmin.site.register(Express,ExpressAdmin)