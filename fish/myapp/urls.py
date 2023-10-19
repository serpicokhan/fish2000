from django.urls import path
from myapp.views import *
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView

from . import views

urlpatterns = [
    path(        'login/',        LoginView.as_view(            template_name="myapp/registration/login.html",            ),        name='login'),
    path(        'logout/',        LoginView.as_view(            template_name="myapp/registration/logout.html",            ),        name='logout'),

    path('', index, name='index'),
    path('userlogin/', user_login2, name='user_login'),
    
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
    url(r'^personel/files/(?P<id>\d+)/remove$', remove_person_file, name='remove_person_file'),
    url(r'^personel/files/$', login_to_load_file, name='login_to_load_file'),
    url(r'^personel/$', list_personel, name='list_personel'),
    url(r'^personel/(?P<id>\d+)/profile$', view_profile, name='view_profile'),
    url(r'^personel/Att$', view_att, name='view_att'),
    url(r'^personel/SaveInfo/$', save_personel_att, name='save_personel_att'),
    url(r'^personel/GetMamnager$', get_manager_by_makan, name='get_manager_by_makan'),

    url(r'^personel/LoadDate/$', view_att, name='view_att'),
    url(r'^personel/(?P<id>\d+)/Delete$', delete_personel, name='delete_personel'),
    url(r'^Hozur/create/$', hozur_create, name='hozur_create'),
    url(r'^Hozur/GetTitles/$', getTitle, name='getTitle'),
    url(r'^Hozur/Calendar/$', show_hozur_calendar, name='show_hozur_calendar'),
    url(r'^Hozur/GetInfo/$', get_personel_calendar_info, name='get_personel_calendar_info'),
    url(r'^Hozur/GetDetails/$', get_hozur_list_detail, name='get_hozur_list_detail'),
    url(r'^Profile/Create/$', personel_create, name='create_profile'),
    url(r'^Profile/(?P<id>\d+)/Update/$', update_personel, name='update_personel'),
    url(r'^personel/Search/$',search_personel,name='search_personel'),
    url(r'^Hozur/Success/$',show_hozur_success,name='show_hozur_success'),







]
