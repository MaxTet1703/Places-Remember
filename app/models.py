from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


# Create your models here.
class UserImageModel(models.Model):
    """
    Model for storage users' image
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="image", verbose_name="Пользовтель")
    image = models.ImageField(upload_to="user_profiles/", verbose_name="Изображение")


class PlaceModel(models.Model):
    """
    Model for storage users' reviews about places
    """
    name = models.TextField(null=False, blank=False, max_length=60, verbose_name="Название места")
    description = models.TextField(null=False, blank=False, max_length=500, verbose_name="Описание")
    longitude = models.FloatField(null=False, blank=False, verbose_name="Широта")
    latitude = models.FloatField(null=False, blank=False, verbose_name="Долгота")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def get_absolute_url(self):
        return reverse_lazy("change", kwargs={"id": self.pk})