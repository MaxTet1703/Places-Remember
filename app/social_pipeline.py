"""
Module where there is the social pipeline's component for vk authentication
"""
from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
import vk_api

from .models import UserImageModel


def get_image(strategy, details, backend, user=None, *args, **kwargs):
    """
    Getting user's image after successful sign in
    """
    if user:
        if not UserImageModel.objects.filter(user=user).exists():
            extra_data = user.social_auth.all().first()
            access_token = extra_data.extra_data["access_token"]
            api = vk_api.VkApi(token=access_token).get_api()
            photo_url = api.users.get(user_ids=extra_data.uid, fields='photo_max_orig')[0]['photo_max_orig']
            img_temp = NamedTemporaryFile(delete=False)
            img_temp.write(urlopen(photo_url).read())
            img_temp.flush()
            new_image = UserImageModel(user=user)
            new_image.image.save(f"image_{user.pk}.jpg", File(img_temp))
            new_image.save()
