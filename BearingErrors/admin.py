from django.contrib import admin

# Register your models here.
admin.site.site_header = '轴承管理后台'  # 设置header
admin.site.site_title = '轴承管理后台'   # 设置title
admin.site.index_title = '轴承管理后台'
from .models import Task
admin.site.register(Task)