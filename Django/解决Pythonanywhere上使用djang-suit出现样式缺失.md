## 解决Pythonanywhere上使用djang-suit出现样式缺失
替换完代码,执行`python manage.py collectstatic`后
可能由于之前收集过,所以产生了

	django file upload: [Errno 13] Permission denied: '/static'

的错误,但是不需要管,报错还是已经收集完成的
修改的主页和一些页面也都可以正常显示(有的需要清除缓存或者Chrome使用Shift+F5强制刷新一下),
但是高兴没多久,问题就来了,django-suit所替换的admin后台始终找不到静态文件.解决方案如下:

1. 卸载django-suit,是的,就是卸载

    	$:pip uninsatall django-suit
    	$:pip install https://github.com/darklow/django-suit/tarball/v2
        # 安装django-suit v2,对Django2.x和Python3.x有更好的支持和更好的界面
		# 在requirements.txt中：
        -e git://github.com/darklow/django-suit.git@v2#egg=django-suit

2. 之前的配置暂时不用改:[django-suit配置](#settings)
3. 在pythonanywhere的控制台打开python,找到django静态文件的目录

		>> import django
		>> django.__file__
		'/home/LIUYA/venv/lib/python3.6/site-packages/django/__init__.py'
4. 找到根目录后我需要的绝对路径为`/home/LIUYA/venv/lib/python3.6/site-packages/django/contrib/admin/static/`,修改settings文件为:

		STATIC_ROOT = '/home/LIUYA/venv/lib
        				/python3.6/site-packages/django/contrib/admin/static/'
		STATIC_URL = '/static/'

    static在url.py中的配置不变:

    	from django.conf.urls.static import static
        ...
        urlpatterns = [...]
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
5. 最后一步,更改pythonanywhere的web选项卡中的Static files,将Url设置为`/static/`,Directory为刚刚的路径`/home/LIUYA/venv/lib/python3.6/site-packages/django/contrib/admin/static/`

**齐活**

### <span id="settings">django-suit的配置使用</span>
1. 安装
	建议直接和上述一样安装suit-v2,这里不再赘述
2. 配置settings

		INSTALLED_APPS = [
        'suit',  # 添加suit支持,一定要放在admin上面,不然打开的还是原有的后台
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'web_sso',
        ]
        ......
        LANGUAGE_CODE = 'zh-Hans'  # 设置成中文简体,繁体为zh-hans
        TIME_ZONE = 'Asia/Shanghai'
        USE_I18N = True
        USE_L10N = False  # 注意是False 配合下边时间格式
        USE_TZ = False  # 如果只是内部使用的系统，这行建议为false，不然会有时区问题
        DATETIME_FORMAT = 'Y-m-d H:i:s'  # suit在admin里设置时间的一个小bug。需要把时间格式指定一下
        DATE_FORMAT = 'Y-m-d'
        ......
        SUIT_CONFIG = {  # suit页面配置
            'ADMIN_NAME': 'EVIC',  #登录界面提示
        }
很对的配置文章中提到需要添加request:

		TEMPLATES = [
   		{
        ...
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # 就是这条
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            	],
        	},
    	},
		]
但其实django2.x是自带的,如果需要,也可以添加



