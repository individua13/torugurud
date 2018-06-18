DEBUG=False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_paycopg2',
        'NAME': 'db1',
		'USER': 'torugurud',
		'PASSWORD': 'Django_test',
		'HOST': 'localhost',
		'PORT': '',
    }
}
