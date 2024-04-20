import os

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import UserImageModel, PlaceModel
from .forms import PlacesForm

# Create your views here.


def start_page(request):
    """
    Application's entrypoint
    """
    return render(request, 'startpage.html')


class MainPageView(LoginRequiredMixin, ListView, FormView):
    """
    Main page where there are the list of reviews and form for adding new reviews
    """
    template_name = 'main.html'
    model = PlaceModel
    context_object_name = "reviews"
    form_class = PlacesForm

    def get_queryset(self, *args, **kwargs):
        return PlaceModel.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['photo'] = UserImageModel.objects.get(user=self.request.user)
        context["key_api"] = os.getenv("YANDEXMAPKEY")
        return context

    def form_valid(self, form):
        new_entry = form.save(commit=False)
        new_entry.user = self.request.user
        new_entry.save()
        return JsonResponse({"status": 200}, status=200)

    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status": 400}, status=400)


def logout_user(request):
    """
    View function for logout
    """
    logout(request)
    return redirect('login')
