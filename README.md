
django-admin start "NAME_PROJECT"

ingresar a la carpeta "NAME_PROJECT"

## Para comenzar hacer el proyecto

python manage.py migrate

Crear el archivo "celery.py" segun code y layout indicado en la pagina "First Step Celery Django"

Modificar el archivo __init__ segun lo idnicado en "First Step Celery Django"

## Para hacer correr el codigo

cd Desktop/Celery-Vim/my_celery

/home/ubuntu/.local/bin/celery -A my_celery worker -l info

/home/ngempin/.local/bin/celery -A my_celery worker -l info

## Para correr en forma manual
python manage.py shell

## Para adjuntar el broker
Modificar el archivo "Settings" indicando CELERY_BROKER_URL. En mi caso Redis

## Para crear la app
python manage.py startapp "APP" => para crear la app

Crear archivo "Tasks.py" dentro de la carpeta "APP"

En archivo "Settings.py" indicar en notificaciones la carpeta "APP"

## Agregar beat y results
pip install django_celery_beat, agregar en archivo de "Settings" en menu INSTALLED_APPS.
volver a ejecutar el comando python migrate.py migrate

pip install django-celery-results, agregar en archivo de "Settings" en menu INSTALLED_APPS.
volver a ejecutar el comando python migrate.py migrate

## Comandos para activar celery
python manage.py shell => para hacer pruebas con las tareas desde la consola de Python

python manage.py runserver => para hacer correr el servidor

pip install django-celery-results, indicar en notificaciones la carpeta "APP". Ejecutar
python manage.py migrate, ejecutar python manage.py inspectdb y ver los cambios. 
python manage.py inspectdb => para revisar el avance de las confirguraciones

## Colocar en la carpeta de Settings
CELERY_BROKER_URL = 'redis://:pc287beea8ef0cfa90c119ab32ee685c2bd8f85c4414634dc511b5bcc5e13dbb0@ec2-52-55-138-195.compute-1.amazonaws.com:29239'  
Segun lo que diga REDIS_URL, colocar en CELERY_BROKER_URL

CELERY_RESULT_BACKEND='django-db'                                                                                                                        
CELERY_CACHE_BACKEND='django-cache'


pip install django-celery-beats, indicar en notificaciones la carpeta "APP". Ejecutar
python manage.py migrate, ejecutar python manage.py inspectdb y ver los cambios.

python manage.py inspectdb => para revisar el avance de las confirguraciones


Para controlar el beat, se ejecuta este comando
/home/ngempin/.local/bin/celery -A my_celery beat -l info
Anteriormente en setting debe estar activada esta opcion de django_celery_beat

Agregar otro usuario mas
/home/ngempin/.local/bin/celery -A my_celery worker -n pico@pico.com

Monitoreo de las operaciones
/home/ngempin/.local/bin/celery -A my_celery status



/home/ngempin/.local/bin/celery -A my_celery inspect active

Simple
```
from robots.tasks import get_rand
result=get_rand.delay()
```

result

result.get()

Chain
```
from celery import chain
from robots.tasks import sum
res=chain(sum.s(4,2),sum.s(5),sum.s(21))()
res.get()
res.parent.get()
res.parent.parent.get()
```

```
result=sum.delay(2,3)
result
result.get()
```



