# Module to don't repeat code
import os 

from .models import UserImageModel


class DatamixIn:
    """
        MixIn to get key api for yandex map and user's image
    """
    @property
    def get_data(self):
        return {
            'key_api': os.getenv("YANDEXMAPKEY"),
            'photo': UserImageModel.objects.get(user=self.request.user)
        }

