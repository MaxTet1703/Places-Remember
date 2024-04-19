from django.urls import path 

from .views import start_page, logout_user, main_page

urlpatterns = (
    path('', start_page, name="login"),
    path('main/', main_page, name='main'),
    path('logout/', logout_user, name='logout')
)