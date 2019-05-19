[Join and Contact us on Discord](https://discord.gg/avmdZJa)

------

#### How to use this project in my project ?

Firstly, we need to set up the libraries that in requirements files.

after we need to set up this project.

```python
pip install -r requirements.txt
pip install steemconnect_auth
```

open a new steem application in this address, [https://v2.steemconnect.com/apps/me](https://v2.steemconnect.com/apps/me) like this
<br>
![1.JPG](https://cdn.steemitimages.com/DQmUuKDj9mzR29bKkXq6Z7r7uaVT1Q3NV6QuBFTGe3WE4Qh/1.JPG)

Set up your Django project and open your project's settings.py file, you must set the following codes by your project, django_steemconnect uses these settings.

```python
##steemconnect settings
STEEMCONNECT_AUTH_CONFIGS = dict(
    redirect_url="http://www.coogger.com/accounts/steemconnect/",
    client_id="coogger.app",
    app_secret="your app secret",
    scope="login,offline,vote,comment,delete_comment,comment_options,custom_json,claim_reward_balance",
    code=True,
    login_redirect="/",
)

# if you want to access in any template this STEEMCONNECT_AUTH_CONFIGS
MIDDLEWARE += ["steemconnect_auth.middleware.steemconnect_auth.SteemConnectAuthMiddleware"]
# {{ request.steemconnect_auth.client_id }}
# {{ request.steemconnect_auth.app_secret }}

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

urlpatterns = [
    url(r"^",include("myapp.urls")),
    url(r"^accounts/", include('steemconnect_auth.urls')), # signup, login or create new user
    url(r'^web/admin/', admin.site.urls), # admin panel
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

##### if access_token expires, you should use this function should be used.

```python
from steemconnect_auth.models import SteemConnectUser

steem_connect_user = SteemConnectUser.objects.filter(user="username")
new_access_token = steem_connect_user.update_access_token("your app secret")
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
