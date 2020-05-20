from django.contrib import admin
from django.urls import path
from . import views

app_name = 'alarmapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('sweety',views.sweety,name='sweety'),
    path('timetables', views.timetables , name='timetables'),
    path('modify_timetable',views.modify_timetable,name='modify_timetable'),
    path('subject/',views.subject,name='subject'),
    path('subject/add_subject',views.add_subject,name='add_subject'),
    path('subject/delete_subject',views.delete_subject,name='delete_subject'),
    path('show_urls/',views.show_urls,name='show_urls'),
    path('show_urls/add_url',views.add_url,name='add_url'),
    path('show_urls/delete_url',views.delete_url,name='delete_url'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]
