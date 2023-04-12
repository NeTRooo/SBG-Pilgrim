from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.login_page, name='login_page'),
    re_path('^tgauth/otp/(?P<encrypted>.+)/$', views.tgauth, name='tgauth'),
    path('profile/', views.profile_page, name='profile_page'),
    path('check/', views.check_page, name='check_page'),
    path('applications/', views.applications_page, name='applications_page'),
    path('help/', views.help_page, name='help_page'),
    path('settings/', views.settings_page, name='settings_page'),
    path('logout/', views.custom_logout, name='custom_logout'),
]
