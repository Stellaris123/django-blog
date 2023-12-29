"""
models.py - 该模块定义了两个 Django 模型
[1]UserProfile (用户配置文件)
    1.扩展默认的 User 模型
[2]EmailVerifyRecord (电子邮件验证记录模型)
    1.电子邮件验证记录的管理
"""
# Django 模型引入
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 用户配置文件模型
class UserProfile(models.Model):
    # 用户性别选择项
    USER_GENDER_TYPE = (
        ("male", "男"),
        ("female", "女"),
    )

    # 与内置用户模型一对一的关系，用于扩展用户信息
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")
    nike_name = models.CharField("昵称", max_length=23, blank=True, default="")
    desc = models.TextField("个人简介", max_length=200, blank=True, default="")
    gexing = models.CharField("个性签名", max_length=100, blank=True, default="")
    birthday = models.DateField("生日", null=True, blank=True)
    gender = models.CharField("性别", max_length=6, choices=USER_GENDER_TYPE, default="male")
    address = models.CharField("地址", max_length=100, blank=True, default="")
    image = models.ImageField(upload_to="images/%Y/%m", default="images/default.png", max_length=100, verbose_name = "用户头像")

    class Meta:
        verbose_name = "用户数据"
        verbose_name_plural = verbose_name
    
    # 在管理员界面中显示用户对象的用户名
    def __str__(self):
        return self.owner.username


# 电子邮件验证记录模型
class EmailVerifyRecord(models.Model):
    # 发送类型选择项
    SEND_TYPE_CHOICES = (
        ("register", "注册"),
        ("forget", "找回密码")
    )

    # 验证码、邮箱和发送类型的字段
    code = models.CharField("验证码", max_length=20)
    email = models.EmailField("邮箱", max_length=35)
    send_type = models.CharField(choices=SEND_TYPE_CHOICES, default="register", max_length=20)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
    
    # 在管理员界面中显示验证码字符串
    def __str__(self):
        return self.code