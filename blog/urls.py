from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from account import views as Ac
from blog import views



urlpatterns = [
    path('', views.index, name='index'),
    path('why', views.why, name='why'),
    path('preschool', views.preschool, name='preschool'),
    path('primaryschool', views.primaryschool, name='primaryschool'),
    path('secondaryschool', views.secondaryschool, name='secondaryschool'),
    path('schoolprogram', views.schoolprogram, name='schoolprogram'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('registration', views.registration, name='registration'),
    path('openhours', views.openhours, name='openhours'),
    path('admission', views.admission, name='admission'),
    path('add_post', views.add_post, name='add_post'),
    path('accounts/delete_new_post/<int:post_id>', views.delete_new_post, name='delete_new_post'),
    path('accounts/edit_new_post/<int:post_id>', views.edit_new_post, name='edit_new_post'),
    path('sitemessages', views.sitemessages, name='sitemessages'),
    path('all_messages', views.all_messages, name='all_messages'),
    path('schoolinfos', views.schoolinfos, name='schoolinfos'),
    path('accounts/view_message/<int:sitemessage_id>', views.view_message, name='view_message'),
    # path('edit_post/<int:article_id>', views.edit_post, name='edit_post'),
    path('view_post/<int:article_id>', views.view_post, name='view_post'),

    path('form1_application', views.form1_application, name='form1_application'),
    path('Form2_4_application', views.Form2_4_application, name='Form2_4_application'),
    path('LowerSixth_application', views.LowerSixth_application, name='LowerSixth_application'),
    path('Nursery_application', views.Nursery_application, name='Nursery_application'),
    path('Class2_6_application', views.Class2_6_application, name='Class2_6_application'),
    path('Class1_application', views.Class1_application, name='Class1_application'),
    path('Teacher_application', views.Teacher_application, name='Teacher_application'),
    path('view_applications', views.view_applications, name='view_applications'),

    path('l6_app_view/<int:l6_id>', views.l6_app_view, name='l6_app_view'),
    path('l6_app_accept/<int:l6_id>', views.l6_app_accept, name='l6_app_accept'),
    path('f1_app_view/<int:f1_id>', views.f1_app_view, name='f1_app_view'),
    path('f1_app_accept/<int:f1_id>', views.f1_app_accept, name='f1_app_accept'),
    path('f2_4_app_view/<int:l6_id>', views.f2_4_app_view, name='f2_4_app_view'),
    path('f2_4_app_accept/<int:l6_id>', views.f2_4_app_accept, name='f2_4_app_accept'),

    path('c2_6_app_view/<int:f1_id>', views.c2_6_app_view, name='c2_6_app_view'),
    path('c2_6_app_accept/<int:f1_id>', views.c2_6_app_accept, name='c2_6_app_accept'),

    path('c1_app_view/<int:f1_id>', views.c1_app_view, name='c1_app_view'),
    path('c1_app_accept/<int:f1_id>', views.c1_app_accept, name='c1_app_accept'),

    path('n_app_view/<int:f1_id>', views.n_app_view, name='n_app_view'),
    path('n_app_accept/<int:f1_id>', views.n_app_accept, name='n_app_accept'),
    path('t_app_view/<int:f1_id>', views.t_app_view, name='t_app_view'),
    path('t_app_accept/<int:f1_id>', views.t_app_accept, name='t_app_accept'),

    path('thankyou', views.thankyou, name='thankyou'),
    path('loging', Ac.loging, name='loging'),
]
