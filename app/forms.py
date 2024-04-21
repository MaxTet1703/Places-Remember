from django.core.exceptions import ValidationError
from django import forms

from .models import PlaceModel


class PlacesForm(forms.ModelForm):
    """
    Form for creating reviews
    """
    class Meta:
        model = PlaceModel
        coords = forms.NumberInput(attrs={'type': 'hidden'})
        fields = ("name", "description", "latitude", "longitude")

    def clean_name(self):
        """
        name's field validation
        """
        name = self.data["name"]
        if not name:
            raise ValidationError("name is blank")
        return name

    def clean_description(self):
        """
        description's field validation
        """
        desrc = self.data.get("description")
        if not desrc:
            raise ValidationError("description is blank")
        return desrc

    def clean_latitude(self):
        """
        latitude's field validation
        """
        lat = self.data.get("latitude")
        if not -180.0 <= float(lat) <= 180.0:
            raise ValidationError("Value is not in correct range")
        return lat

    def clean_longitude(self):
        """
        longitude's field validation
        """
        longitude = self.data.get("longitude")
        print(longitude)
        if not -90.0 <= float(longitude) <= 90.0:
            raise ValidationError("Value is not in correct range")
        return longitude