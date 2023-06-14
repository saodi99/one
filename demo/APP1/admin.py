from django.contrib import admin

# Register your models here.
from . import models

class User_m(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('id','name', 'email','sex',
              'c_time','message',
              'avater',)
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    list_display_links = ('name',)
    # 设置过滤选项
    list_filter = ('c_time',)
    # 每页显示条目数 缺省值100
    list_per_page = 50
    # show all页面上的model数目，缺省200
    # list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    list_editable = ('email',"sex")
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按发布日期降序排序
    ordering = ('-c_time',)
    # 搜索条件设置
    search_fields = ('name',)

    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name=u"姓名")

    # 字段关联展示
    ## 场景1、关联其他表的数据展示，此处外键展示不做演示，生产环境尽量减少外键使用

    ## 场景2、枚举信息转义展示
    ###  此处需要在model定义页面通过枚举值转义配置对应展示中文信息,参考model模块代码设置

    """
      这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
      但是还是可以通过手动输入url的方式来进入编辑页面。
      不过可以配合设置fieldsets或者readonly_fieldss来达到目的
      注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
    """
    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return True



class Goods_m(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('name','c_time','level',
              'remark','price',"sort","count","display","uid",
              'image',)
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    list_display_links = ('name',)
    # 设置过滤选项
    list_filter = ('c_time',)
    # 每页显示条目数 缺省值100
    list_per_page = 50
    # show all页面上的model数目，缺省200
    # list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    list_editable = ("display",)
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按发布日期降序排序
    ordering = ('-c_time',)
    # 搜索条件设置
    search_fields = ('name',)

    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name=u"姓名")

    # 字段关联展示
    ## 场景1、关联其他表的数据展示，此处外键展示不做演示，生产环境尽量减少外键使用

    ## 场景2、枚举信息转义展示
    ###  此处需要在model定义页面通过枚举值转义配置对应展示中文信息,参考model模块代码设置

    """
      这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
      但是还是可以通过手动输入url的方式来进入编辑页面。
      不过可以配合设置fieldsets或者readonly_fieldss来达到目的
      注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
    """
    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return True



admin.site.register(models.User,User_m)
admin.site.register(models.Bought_goods)
admin.site.register(models.Goods,Goods_m)
admin.site.register(models.Goods_message)
admin.site.register(models.Passwrd)
admin.site.register(models.Shopping_cart)
admin.site.register(models.Post_goods)


admin.site.site_header = '校园二手交易管理后台'  # 设置header
admin.site.site_title = '校园二手交易管理后台'   # 设置title
admin.site.index_title = '校园二手交易管理后台'




