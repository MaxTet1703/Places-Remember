from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import ListView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import PlaceModel
from .mixin import DatamixIn
from .forms import PlacesForm

# Create your views here.


def start_page(request):
    """
    Application's entrypoint
    """
    return render(request, 'startpage.html')


class MainPageView(LoginRequiredMixin, DatamixIn, ListView, FormView):
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
        return context | self.get_data

    def form_valid(self, form):
        new_entry = form.save(commit=False)
        new_entry.user = self.request.user
        new_entry.save()
        return JsonResponse({"message": "Впечатление было успешно создано",
                            "status": 200}, status=200)

    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status": 400}, status=400)


class ChangeReviewView(LoginRequiredMixin, DatamixIn, View):
    """
        Page for review change
    """
    @property
    def get_context_data(self):
        context = {
            'data': PlaceModel.objects.get(pk=self.kwargs["id"]),
        }
        return context | self.get_data

    def get(self, request, id):
        if not PlaceModel.objects.filter(pk=id, user=self.request.user).exists():
            return redirect("main")
        return render(request, 'change.html', context=self.get_context_data)

    def post(self, request, id):
        form = PlacesForm(self.request.POST)
        if form.is_valid():
            entry = PlaceModel.objects.get(pk=id)
            entry.name = form.cleaned_data["name"]
            entry.description = form.cleaned_data["description"]
            entry.longitude = form.cleaned_data["longitude"]
            entry.latitude = form.cleaned_data["latitude"]
            entry.save()
            return JsonResponse({"message": "Изменение сохранено успешно",
                                "status": 200}, status=200)
        return JsonResponse({"status": 400}, status=400)


def logout_user(request):
    """
    View function for logout
    """
    logout(request)
    return redirect('login')
