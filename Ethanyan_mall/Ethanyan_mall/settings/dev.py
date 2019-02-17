"""
Django settings for Ethanyan_mall project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import datetime
import os
import sys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将apps添加到搜索包目录列表中
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
# print(sys.path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jl#33@sr^=!p(s@46b2&k4kost(@!k-#qtnjo$%ixenxlwb9i2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api.meiduo.site', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'django_crontab',  # 定时任务
    'pics.apps.PicsConfig',
    'haystack',
    # 以后将安装的包放在上面，应用的包放在下面
    # 'Ethanyan_mall.apps.users.apps.UsersConfig',
    'users.apps.UsersConfig',
    'verifications.apps.VerificationsConfig',
    'oauth.apps.OauthConfig',
    'areas.apps.AreasConfig',
    'contents.apps.ContentsConfig',
    'goods.apps.GoodsConfig',
    'cart.apps.CartConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Ethanyan_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 设置模板文件目录
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Ethanyan_mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'meiduo',  # 数据库用户名
        'PASSWORD': 'meiduo',  # 数据库用户密码
        'NAME': 'meiduo_mall'  # 数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 语言时区本地化
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# 设置Django框架的缓存位置（如果不做设置，缓存默认是服务器内存)
# 此处是要把Django框架的缓存改为redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 设置redis数据库地址
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 设置redis数据库地址
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "verify_codes": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 设置redis数据库地址
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 保存用户浏览记录
    "histories": {
        "BACKEND": "django_redis.cache.RedisCache",
        # celery中我们使用了3号库，这里修改为4
        "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
# from redis import StrictRedis
# StrictRedis(host='127.0.0.1',port=6379,db=2)
# from django_redis import get_redis_connection
# redis_conn = get_redis_connection('verify_code') # StrictRedis对象
# 设置将Django框架的session存储到缓存中，上面已经把Django框架的缓存改为了redis
# 所以session就存储到了redis中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 设置session存储到缓存空间的名称
SESSION_CACHE_ALIAS = "session"

# django框架的日志存储设置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 此处的BASE_DIR指的是内层的Ethanyan_mall的地址
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/meiduo.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            # 打印日志的格式，在上面定义了。找对应的名称查看
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}
# 打印日志
# import logging
# 获取日志器
# logger = logging.getLogger('django')
# 调用日志器的方法进行对应处理
# logger.debug('Debug Message')
# logger.info('info Message')
# logger.error('Error Message')
# logger.warning('warning Message')
# logger.fatal('fatal Message')

REST_FRAMEWORK = {
    # 指定DRF框架异常处理的函数
    'EXCEPTION_HANDLER': 'Ethanyan_mall.utils.exceptions.exception_handler',
    # 认证设置
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 引入JWT认证机制，之后客户端请求服务器时，如果传递jwt token
        # 此认证机制会自动校验jwt token的有效性，如果无效直接返回401(未认证)
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 全局分页设置
    'DEFAULT_PAGINATION_CLASS': 'Ethanyan_mall.utils.pagination.StandardResultPagination',
}
# JWT扩展配置
JWT_AUTH = {
    #　设置JWT的有效时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 指定jwt扩展登录视图响应数据函数
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'users.utils.jwt_response_payload_handler'
}

# 我们自定义的用户模型类还不能直接被Django的认证系统所识别，需要在配置文件中告知Django认证系统使用我们自定义的模型类。
# AUTH_USER_MODEL = '子应用.模型类'
AUTH_USER_MODEL = 'users.User'

# CORS白名单设置
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    'www.meiduo.site:8080',
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie


# 只等django认证系统的后端类
AUTHENTICATION_BACKENDS = ['users.utils.UsernameMobileAuthBackend']

# QQ登录参数
QQ_CLIENT_ID = '101474184' # 开发应用APPid
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c' # 开发应用的APP-KEY
QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html' # 回调网址
QQ_STATE = '/' # 登录之后跳转的页面地址

# 邮箱发送配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务器地址
EMAIL_HOST = 'smtp.163.com'
# SMTP服务器端口
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = 'testokpass@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'MEIyoumima789'
#收件人看到的发件人
EMAIL_FROM = '闫氏商城<testokpass@163.com>'

# DRF扩展
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

# FastDFS
# FDFS文件存储配置
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')

# FDFS Nginx的地址
FDFS_NGINX_URL = 'http://image.meiduo.site:8888/'

# 设置Django文件系统的存储类
DEFAULT_FILE_STORAGE = 'Ethanyan_mall.utils.fastdfs.fdfs_storage.FDFSStorage'

# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''

# 生成的静态html文件保存目录
GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc')

# 定时任务设置
CRONJOBS = [
    # 每1分钟执行一次生成主页静态文件
    ('*/1 * * * *', 'contents.crons.generate_static_index_html', '>> ' + os.path.dirname(BASE_DIR) + '/logs/crontab.log')
]

# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

# Haystack全文检索框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 指定所使用的搜索引擎
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        # 指定es搜索引擎服务器地址
        'URL': 'http://192.168.59.225:9200//',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        # 指定elasticsearch建立的索引库的名称
        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'