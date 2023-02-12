from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('placement',views.placement,name='placement'),
    path('pythond',views.pythond,name='pythond'),
    path('pythonat',views.pythonat,name='pythonat'),
    path('pythonmt',views.pythonmt,name='pythonmt'),
    path('sql',views.sql,name='sql'),
    path('web',views.web,name='web'),
    path('apti',views.apti,name='apti'),
    path('verbal',views.verbal,name='verbal'),
    path('contact',views.contact,name='contact'),
    path('fresher',views.fresher,name='fresher'),
    path('experience',views.experience,name='experience'),
]
