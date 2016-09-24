First app in django
=====================
[![django](https://s3-eu-west-1.amazonaws.com/glynjacksonorg/assets/powered-by.jpg)](https://docs.djangoproject.com/es/)

'Escribiendo su primera aplicación en Django' [Reference](https://docs.djangoproject.com/es/1.10/intro/tutorial01/)

#### Before install
```sh
$ python --version
$ python -m django --version
```

### Install
```sh
$ sudo easy_install pip
$ sudo pip install virtualenv
$ cd Documents/projects
$ virtualenv name_project
$ cd name_project
$ source bin/activate
$ pip install Django==1.10.1
$ pip freeze  (return all installed dependencies into virtualenv)
```

#### Update versions
```sh
$ pip install --upgrade pip
$ pip install --upgrade django
```

### 1-  First stage (v.0.1):
* project `start up` (firstDjango)
* `DB` configuration (sqlite3)
* `URL` configuration (admin)
* crate application (app)
* `models` configuration (Data)    
* DB synchronization
* run server
* accessing to localhost:8000/admin

### 2- 	Second stage (v.0.2):
* `templates` creation
* `urls` and `views` configuration
* add data in `admin`
* sending data between views through models
* show data into the templates.


#### Create a project - First stage

```sh
$ django-admin startproject myproject
$ cd myproject
$ python mange.py runserver  or python manage.py runserver 0.0.0.0:8000
```


>
> Luego de crear un proyecto, este puede contener varias aplicaciones.
>



Por ejemplo luego de crear 'myproject', este puede contener una app (ej: polls)

```sh
// desde donde se encuentra manage.py
$ python manage.py startapp polls
```

* crear la vista dentro de (view.py)
* asignar la vista a una url (urls.py)
* realizar un import de polls/url.py en myproject/urls.py
