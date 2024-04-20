from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserImageModel, PlaceModel

# Create your views here.


def start_page(request):
    """
    Application's entrypoint
    """
    return render(request, 'startpage.html')


class MainPageView(LoginRequiredMixin, ListView):
    template_name = 'main.html'
    model = PlaceModel
    context_object_name = "reviews"

    def get_queryset(self, *args, **kwargs):
        return PlaceModel.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['photo'] = UserImageModel.objects.get(user=self.request.user)
        return context
    pass


# def main_page(request):
#     """
#     Main page for loggined users
#     """
#     return render(request, 'main.html')


def logout_user(request):
    """
    View function for logout
    """
    logout(request)
    return redirect('login')
