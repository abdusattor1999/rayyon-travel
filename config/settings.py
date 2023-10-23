# 1 : create model for customers
# 2 : fix views to Put customer and commenters seperately
# 3 : remove sign from footer
# 4 : edit footer url to home_page
# 5 : fix send_email func
  

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xhuc68zgrr(fh=d&n2u5%t0$w*j_43)vy*$_6z3gpwkoodqoa7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rosetta',
    # internal
    "corsheaders",
    'account',
    'posts',

    # external
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rayhonto_db',
        'USER': 'rayhonto_db_user',
        'PASSWORD': 'j{WJ_^q$$oiO',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Rayyon Travel Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Rayyon",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Rayyon Tour",

    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "static/img/logo.png",

    "welcome_sign": "Admin panelga kirish",
    "copyright": "@abdusattor_abdulboqiyev",
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

CORS_ALLOWED_ORIGINS = [
    "https://fa3a-213-230-76-94.ngrok-free.app",
    "https://www.rayhontour.uz"
]
CSRF_TRUSTED_ORIGINS = [
    "https://fa3a-213-230-76-94.ngrok-free.app",
    "https://www.rayhontour.uz"
]

# CORS_ALLOW_ALL_ORIGINS=True

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('uz', _("O'zbek")),
    ('ru', _('Russian'))
]
LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


LOCALE_PATHS = os.path.join(BASE_DIR, "locale/"),

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'
STATIC_ROOT = 'assets/'
# STATIC_DIRS = [str(BASE_DIR.joinpath('static'))]
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
MEDIA_URL = 'media/'
MEDIA_ROOT = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'server3.ahost.uz'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'teenagers.data@gmail.com'
EMAIL_HOST_PASSWORD = 'ahpc rvwo wlxl qsle'



LOGIN_REDIRECT_URL = 'posts:home_page'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'posts:home_page'



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)