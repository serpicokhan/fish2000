from django.urls import path
from myapp.views import *
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView

from . import views

urlpatterns = [
    path(        'login/',        LoginView.as_view(            template_name="myapp/registration/login.html",            ),        name='login'),
    path(        'logout/',        LoginView.as_view(            template_name="myapp/registration/logout.html",            ),        name='logout'),

    path('', index, name='index'),
    url(r'^User/$',list_user,name='list_user'),
    url(r'^User/create/$', user_create, name='user_create'),
    url(r'^User/(?P<id>\d+)/update/$', user_update, name='user_update'),
    url(r'^User/(?P<id>\d+)/delete/$', user_delete, name='user_delete'),
    url(r'^Folder/$', list_folder, name='list_folder'),
    url(r'^Mail/$',list_mail,name='list_mail'),
    url(r'^Fish/$',list_fish,name='list_fish'),
    url(r'^Fish/Search/$',search_fish,name='search_fish'),
    url(r'^Fish/Upload$',fish_upload,name='fish_upload'),
    url(r'^Fish/Create$',fish_create,name='fish_create'),
    url(r'^Fish/Detail$',details_fish,name='details_fish'),
    url(r'^Mail/create/$', mail_create, name='mail_create'),
    url(r'^Fish/(?P<id>\d+)/shekayat/$', register_shekayat, name='register_shekayat'),
    url(r'^Mail/(?P<id>\d+)/delete/$', mail_delete, name='mail_delete'),
    url(r'^Mail/(?P<id>\d+)/update/$', mail_update, name='mail_update'),
    url(r'^Mail/Sent/$', list_sentmail, name='list_sentmail'),
    url(r'^Mail/Status/$', list_unread_mail, name='list_unread_mail'),
    url(r'^Mail/System/$', list_sysmail, name='list_sysmail'),
    url(r'^MailFile/$', file_upload, name='file_upload'),
    url(r'^upload/$', handle_file_upload, name='handle_file_upload'),
    url(r'^file/$', file_upload_doc, name='file_upload_doc'),
    url(r'^personel/upload/$', insert_personel_data_from_csv, name='insert_personel_data_from_csv'),
    url(r'^personel/files/$', login_to_load_file, name='login_to_load_file'),
    url(r'^personel/$', list_personel, name='list_personel'),
    url(r'^personel/profile$', view_profile, name='view_profile'),


]
