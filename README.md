#### How to use this project in my project ?

Firstly, we need to set up the libraries that in requirements files.

```python
pip install django
pip install steem-connect
```

after we need to set up this project.

```python
pip install steemconnect_auth
```

open a new steem application in this address, [https://v2.steemconnect.com/apps/me](https://v2.steemconnect.com/apps/me) like this
<br>
![1.JPG](https://cdn.steemitimages.com/DQmUuKDj9mzR29bKkXq6Z7r7uaVT1Q3NV6QuBFTGe3WE4Qh/1.JPG)

Set up your Django project and open your project's settings.py file, you must set the following codes by your project, django_steemconnect uses these settings.

```python
##steemconnect settings
REDIRECT_URL = "http://www.coogger.com/accounts/steemconnect/"
CLIENT_ID = "coogger.app"
APP_SECRET = "your app secret"
SCOPE = None
# default scopes ="login,offline,vote,comment,delete_comment,comment_options,custom_json,claim_reward_balance"
CODE = True
LOGIN_REDIRECT = "/web/feed/"
##steemconnect settings
```
You should type **REDIRECT_URL** as in the photo below.

![1.JPG](https://cdn.steemitimages.com/DQmRYNKg9z6D9PEmkeSFqiuHpUEjmeEqA36HjrLaqSxgUMQ/1.JPG)

**LOGIN_REDIRECT**, after the user logged in, you should write it to which page you want to redirect it to.

access_token has a limited lifetime, thus if you need to refresh them in your own without authenticating the user again, you can set **CODE** = True.

then, add the django_steemconnect to the list of applications.

```python
INSTALLED_APPS = [
    "myapp",
    "django_steemconnect",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',"
]
```
and finally, add the django_steemconnect URLs to the list of your project URLs.

```python
# /urls.py
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import django_steemconnect

urlpatterns = [
    url(r"^",include("myapp.urls")),
    url(r"^accounts/", include('django_steemconnect.urls')), # signup, login or create new user
    url(r'^web/admin/', admin.site.urls), # admin panel
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```


#### Let's place URLs in a template

##### for logout operation
```
{% url 'logout' %}
```


##### for login operation
```
{% url 'login' %}
```

After all these operations, we must do them for the database settings.

```
python manage.py makemigrations
python manage.py migrate
```

#### fLet's look at the admin panel.

![1.JPG](https://cdn.steemitimages.com/DQmc4FyM4kQ1ZBP8ihDfCp6vWq4E8Aia3A1aiRpWP4Po4so/1.JPG)

----

![2.JPG](https://cdn.steemitimages.com/DQmPkJbQZqr7e99enWg12vVnH4sCoKTbBWdjZ679ZEBxKLF/2.JPG)

----

![3.JPG](https://cdn.steemitimages.com/DQmdj7hL26xpXGQTVdfrQDzkcCqcsQaBWBnYs5ARuUao4Gg/3.JPG)

----

It's all that.
