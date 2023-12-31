"""
forms.py - Django 表单定义
    1.表单(forms)用于处理用户与应用程序之间的数据交互.
    2.收集用户输入的数据, 验证这些数据, 并将其传递给后端处理.
[1]LoginForm (登录表单)
    
[2]RegisterForm (注册表单)
    
[3]ForgetPwdForm (忘记密码表单)

[4]ModifyPwdForm (修改密码表单)

[5]UserForm (用户信息表单)

[6]UserProfileForm (用户配置文件表单)

作者: 李俊霖
日期: 2023.12.6
"""
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

# 登录表单
class LoginForm(forms.Form):
    # 用户名输入框
    username = forms.CharField(label="用户名", max_length=32, widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "用户名/邮箱"
    }))
    
    # 密码输入框
    password = forms.CharField(label="密码", min_length=6, widget=forms.PasswordInput(attrs={
        "class": "input",
        "placeholder": "密码"}))
    
    # 验证密码与用户名是否相同
    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username == password:
            raise forms.ValidationError("用户名与密码不能相同!")
        return password

# 注册表单
class RegisterForm(forms.ModelForm):
    # 邮箱输入框
    email = forms.EmailField(label="邮箱", max_length=32, widget=forms.EmailInput(attrs={
        "class": "input",
        "placeholder": "用户名/邮箱"
    }))
    # 密码输入框
    password = forms.CharField(label="密码", min_length=6, widget=forms.PasswordInput(attrs={
        "class": "input",
        "placeholder": "密码"
    }))
    # 再次输入密码输入框
    password1 = forms.CharField(label="再次输入密码", min_length=6, widget=forms.PasswordInput(attrs={
        "class": "input",
        "placeholder": "再次输入密码"
    }))

    class Meta:
        model = User
        fields = ("email", "password")

    # 验证用户是否存在
    def clean_email(self):
        email = self.cleaned_data.get("email")
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError("用户名已经存在!")
        return email
    
    # 验证密码是否相等
    def clean_password1(self):
        if self.cleaned_data["password"] != self.cleaned_data["password1"]:
            raise forms.ValidationError("两次密码输入不一致!")
        return self.cleaned_data["password1"]

# 忘记密码表单
class ForgetPwdForm(forms.Form):
    # 邮箱输入框
    email = forms.EmailField(label="请输入注册邮箱地址", min_length=4, widget=forms.EmailInput(attrs={
        "class": "input",
        "placeholder": "用户名/邮箱"
    }))

# 修改密码表单
class ModifyPwdForm(forms.Form):
    # 新密码输入框
    password = forms.CharField(label="输入新密码", min_length=6,
        widget=forms.PasswordInput(attrs={
            "class": "input",
            "placeholder": "输入密码"
        }))

# 用户信息表单
class UserForm(forms.ModelForm):
    # 邮箱输入框，禁用
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "input",
        "disabled":"disabled"
    }))

    class Meta:
        model = User
        fields = ("email",)

# 用户配置文件表单
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("nike_name", "desc", "gexing", "birthday", "gender", "address", "image")