from django.urls import path 

from .views import (start_page, logout_user, MainPageView,
                    ChangeReviewView)


urlpatterns = (
    path('', start_page, name="login"),
    path('main/', MainPageView.as_view(), name='main'),
    path('logout/', logout_user, name='logout'),
    path('change/<int:id>/', ChangeReviewView.as_view(), name="change")
)