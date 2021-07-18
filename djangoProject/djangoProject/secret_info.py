# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-mm50%25p1y5dkbqz4x%j)1l#wru(^ycbe!0$kk#a#qep*h7*d'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_project',
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "Localhost",
        "PORT": "3306",
    }
}