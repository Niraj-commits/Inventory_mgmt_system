
Installation requirements

python3 -m venv env
sudo env/bin/activate (always install inside the env)
pip install django
django-admin startproject mainfolder. (keeps all the main details)
python manage.py startapp test (creates new app named test)

(This will help set the project)

(Other required applications)

1. Installing Postgresql
   pip install psycopg2-binary (To help django communicate with database)
   after installing postgres:
   change settings.py database as 
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': '<database-name>',
		'USER':'<database-username>',
		'PASSWORD':'<database-password>',
		'HOST':'localhost',
		'PORT': '5432'
	    }
	}		
2. Installing Debug Toolbar
   - pip install django-debug-toolbar (helps check the stats of project) 
   
   - add to settings.py installed apps as
   
	INSTALLED_APPS = [
	    ...
	    'debug_toolbar',
	]
   
   - in middleware as 
	MIDDLEWARE = [
	   ...
	   "debug_toolbar.middleware.DebugToolbarMiddleware",
	]
   
   - add the conf below at the end of settings.py
	INTERNAL_IPS = [
	    # ...
	    "127.0.0.1",
	    # ...
	]
	
   - add to urls.py as 
	 urlpatterns = [
	   ...
	]+ debug_toolbar_urls()

3. Installing Rest_Framework
   - pip install djangorestframework (installs rest framework inside the venv)
   
   - add to installed apps in settings.py as 
   	INSTALLED_APPS = [
	    ...
	    'rest_framework',
	]

4. Installing dot-env
   -pip install python dot-env (can be used to add data to .env for better security)
   
5. Installing rest_framework.authtoken (For token based authentication)

   - add to installed apps in settings.py as
   	INSTALLED_APPS = [
	    ...
	    'rest_framework.authtoken',
	]
	(remaining for setting.py in last)

6. Installing django-filters

   -pip install django-filters
   
   - add to installed apps in settings.py as
   	INSTALLED_APPS = [
	    ...
	    'django-filters',
	]

7. Installing Documentation Apps

   -pip install def-spectacular
   -pip install drf-spectacular[sidecar] (For Offline mode)
   
   - add to installed apps in settings.py as
   	INSTALLED_APPS = [
	    ...
	    'def_spectacular',
	    'def_spectacular_sidecar'
	]
   -add spectacular setting at the end of settings.py as 
	  SPECTACULAR_SETTINGS = {
	    'TITLE': '<project name>',
    	    'DESCRIPTION': '<project name>',
    	    'VERSION': '1.0.0',
    	    'SERVE_INCLUDE_SCHEMA': False,
	    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
	    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
	    'REDOC_DIST': 'SIDECAR',
	    # OTHER SETTINGS
	}
   -add to urls.py as
  	 from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
	 urlpatterns = [
   		...
    		path('schema/', SpectacularAPIView.as_view(), name='schema'),
    		path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    		path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
	 ]
   -add to settings.py as (also includes settings for Token Authentication)
	   REST_FRAMEWORK = {
	    'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.TokenAuthentication',
	    ],
	    # YOUR SETTINGS
	    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
	}

	   
