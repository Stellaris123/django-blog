from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import UserProfile, EmailVerifyRecord

# 我们看到的这个用户选项就是官方默认通过 UserAdmin 这个类注册到后台的, 那么我们也引入进来, 后边继承这个类
from django.contrib.auth.admin import UserAdmin

# 取消关联注册 User
admin.site.unregister(User)

# 定义关联对象的样式，StackedInline 为纵向排列每一行, TabularInline 为并排排列
class UserProfileInline(admin.StackedInline):
    model = UserProfile   # 关联的模型

# 关联 UserProfile, 这里继承 UserAdmin
class UserProfileAdmin(UserAdmin):
    # 内联UserProfile
    inlines = [UserProfileInline]


# 注册 User 模型
admin.site.register(User, UserProfileAdmin)

@admin.register(EmailVerifyRecord)
class Admin(admin.ModelAdmin):
    """Admin View for """

    list_display = ("code",)
