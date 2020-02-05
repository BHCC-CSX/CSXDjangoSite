import os

DEBUG = True

# SECURE_SSL_REDIRECT = False
# SECURE_CONTENT_TYPE_NOSNIFF = False
# SECURE_BROWSER_XSS_FILTER = False
# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False
# X_FRAME_OPTIONS = 'ALLOW'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Install PyMySQL as mysqlclient/MySQLdb to use Django's mysqlclient adapter
# See https://docs.djangoproject.com/en/2.1/ref/databases/#mysql-db-api-drivers
# for more information
# import pymysql  # noqa: 402
# pymysql.install_as_MySQLdb()


# Running locally so connect to either a local MySQL instance or connect to
# Cloud SQL via the proxy. To start the proxy via command line:
#
#     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
#
# See https://cloud.google.com/sql/docs/mysql-connect-proxy
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'csxdb',
        'USER': os.environ['CSXDB_USER'],
        'PASSWORD': os.environ['CSXDB_PASSWORD']
    }
}
