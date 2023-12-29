"""
Django 项目配置文件 (本文件包含敏感信息)
[1]基本设置:
    - BASE_DIR      (项目路径)
    - SECRET_KEY    (密钥设置)
    - DEBUG         (调试模式设置)
    - ALLOWED_HOSTS (Django 服务主机设置)

[2]应用程序配置:
    - AUTHENTICATION_BACKENDS   (认证后端配置)
    - INSTALLED_APPS            (安装的应用程序列表)

[3]中间件配置:
    - MIDDLEWARE (中间件列表)

[4]URL 配置:
   - ROOT_URLCONF (项目根 URL 配置)

[5]模板配置:
   - 模板引擎及路径配置(TEMPLATES)

[6]WSGI 应用程序配置:
   - WSGI 应用程序路径配置(WSGI_APPLICATION)

[7]数据库配置:
   - 默认数据库设置(DATABASES)

[8]密码验证配置:
   - 密码验证器设置(AUTH_PASSWORD_VALIDATORS)

[9]国际化配置:
   - 语言编码配置(LANGUAGE_CODE)
   - 时区配置(TIME_ZONE)
   - 国际化设置(USE_I18N, USE_L10N, USE_TZ)

[10]静态文件配置:
    - 静态文件 URL 及路径配置(STATIC_URL, STATICFILES_DIRS)

[11]用户上传文件配置:
    - 用户上传文件 URL 及路径配置(MEDIA_URL, MEDIA_ROOT)

[12]邮件配置:
    - 邮件主机、用户名、密码、端口及使用 SSL 配置(EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_SSL)
    - 开发阶段邮件后端配置(EMAIL_BACKEND)
"""
import os

# 项目路径; 例如: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 安全警告: 在生产环境中保持秘密的密钥
SECRET_KEY = "l%3ya7fn3moipdpcltj(tdfcv5^@lj=t5d&72levvls+y*@_4^"
DEBUG = True    # 报错信息: 生产环境中要关闭
ALLOWED_HOSTS = ["*"]   # Django 服务主机设置


AUTHENTICATION_BACKENDS = ( # 应用程序定义
    "users.views.MyBackend",
)
INSTALLED_APPS = [  # 安装的应用程序列表
    "simpleui",
    "django.contrib.admin",         # 管理员站点
    "django.contrib.auth",          # 认证授权系统
    "django.contrib.contenttypes",  # 内容类型框架
    "django.contrib.sessions",      # 会话框架
    "django.contrib.messages",      # 消息框架
    "django.contrib.staticfiles",   # 管理静态文件
    "blog.apps.BlogConfig",         # 博客应用
    "users.apps.UsersConfig",       # 用户应用 (用户中心)
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",   # 这是用来处理用户上传文件
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# 数据库设置
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# 密码验证
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# 国际化设置
LANGUAGE_CODE = "zh-hans"   # 界面语言 (英文: "en-us")
TIME_ZONE = "Asia/Shanghai" # 时区
USE_I18N = True     # 使用国际化
USE_L10N = True     # 使用本地化
USE_TZ = True       # 使用时区


# 静态文件 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = "/static/" # 静态文件路径
STATICFILES_DIRS = [    # 静态文件 url
    os.path.join(BASE_DIR, "static"),
    "/var/www/django-blog/static/",
]
# 用于指定收集静态文件的目标目录。
# 在生产环境中, 部署项目时，需要将所有的静态文件收集到一个同一的目录
# 以便 Web 服务器能够方便地提供这些静态文件
# 在部署时才会用到，开发过程中不需要
# STATIC_ROOT = "/var/www/django-blog/static/"

# 配置用户上传文件
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 发送邮箱配置
EMAIL_HOST = "smtp.163.com"
EMAIL_HOST_USER = "13543074397@163.com"
EMAIL_HOST_PASSWORD = "CRIHSQXDEPAQPTFB"
EMAIL_PORT = 465
EMAIL_USE_SSL = True

# 开发阶段的邮件端
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"