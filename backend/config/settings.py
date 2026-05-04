# """
# Django Settings - Robot Food Delivery App
# """

from pathlib import Path
from datetime import timedelta
import os
STATIC_URL = '/static/'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

from dotenv import load_dotenv
load_dotenv()

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/account/login/'

# # ---------------------------------------------------------------------------
# # Apps
# # ---------------------------------------------------------------------------
# DJANGO_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
# ]

# THIRD_PARTY_APPS = [
#     "rest_framework",
#     "rest_framework_simplejwt",
#     "corsheaders",
#     "django_filters",
#     "channels",      # WebSocket support for real-time robot telemetry
# ]

# LOCAL_APPS = [
#     "apps.accounts",
#     "apps.orders",
#     "apps.robots",
#     "apps.mapping",
#     "apps.navigation",
#     "apps.power",
#     "apps.transactions",
#     "apps.delivery",
# ]

# INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# # ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    # ✅ Required
    'django_otp.middleware.OTPMiddleware',

    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"   # For Django Channels

# # ---------------------------------------------------------------------------
# # Database
# # ---------------------------------------------------------------------------
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("DB_NAME", "robot_delivery"),
#         "USER": os.environ.get("DB_USER", "postgres"),
#         "PASSWORD": os.environ.get("DB_PASSWORD", "postgres"),
#         "HOST": os.environ.get("DB_HOST", "localhost"),
#         "PORT": os.environ.get("DB_PORT", "5432"),
#     }
# }

# # ---------------------------------------------------------------------------
# # Cache & Channel Layers (Redis)
# # ---------------------------------------------------------------------------
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": os.environ.get("REDIS_URL", "redis://localhost:6379/0"),
#     }
# }

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {"hosts": [os.environ.get("REDIS_URL", "redis://localhost:6379/0")]},
#     }
# }

# # ---------------------------------------------------------------------------
# # Auth
# # ---------------------------------------------------------------------------
# AUTH_USER_MODEL = "accounts.User"

# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ],
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.IsAuthenticated",
#     ],
#     "DEFAULT_FILTER_BACKENDS": [
#         "django_filters.rest_framework.DjangoFilterBackend",
#         "rest_framework.filters.OrderingFilter",
#     ],
#     "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
#     "PAGE_SIZE": 20,
# }

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
#     "ROTATE_REFRESH_TOKENS": True,
# }

# # ---------------------------------------------------------------------------
# # CORS
# # ---------------------------------------------------------------------------
# CORS_ALLOWED_ORIGINS = os.environ.get(
#     "CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000"
# ).split(",")

# # ---------------------------------------------------------------------------
# # Static & Media
# # ---------------------------------------------------------------------------
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # ---------------------------------------------------------------------------
# # Robot-specific settings
# # ---------------------------------------------------------------------------
# ROBOT_SETTINGS = {
#     "MAX_SPEED_MS": 1.5,            # metres per second
#     "LOW_BATTERY_THRESHOLD": 20,    # percent
#     "CRITICAL_BATTERY_THRESHOLD": 10,
#     "TELEMETRY_INTERVAL_SECONDS": 2,
#     "MAX_DELIVERY_RADIUS_KM": 5.0,
#     "GEOFENCE_ENABLED": True,
# }
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    # ✅ MFA core
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'two_factor',

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    'channels',
    'config',
    'apps',
]

SITE_ID = 1

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",

]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_SAMESITE = "Lax"

SESSION_COOKIE_SECURE = False 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

#For text vefication
TWILIO_ACCOUNT_SID = "your_sid"
TWILIO_AUTH_TOKEN = "your_token"
TWILIO_PHONE_NUMBER = "+1234567890"