from django.test import TestCase, Client
from django.urls import reverse

from .forms import PlacesForm
from .models import PlaceModel

# Create your tests here.

GOOD_DATA_FOR_FORM = [
    {
        "name": "Бар 'ЧёПоЧём'",
        "description": """Хороший бар, в основном одна молодёжь. Вкусные напитки, хорошая музыка. 
        Персонал вежливый. Думаю еще вернусь сюда. Все понравилось. Отмечали др дочери. Остались довольны""",
        "latitude": 92.213323123,
        "longitude": 56.4234324
    },
    {
        "name": "ДС им. Ивана Ярыгина",
        "description": """Это отлично, что в городе не только появляются новые спортивные объекты, но и реконструируются уже существующие. 
        Была приятно удивлена, когда пришла поболеть за волейбольный клуб Енисей.""",
        "latitude": 86.4535435,
        "longitude": 12.4324324
    }
]
BAD_DATA_FOR_FORM = [
    {
        "name": '',
        "description": """Всё очень понравилось, рекомендую""",
        "longitude": 45.324234,
        "latitude": 103.2323
    },
    {
        "name": "Колизей",
        "description": "",
        "logitude": 12.435343,
        "latitude": 89.31232
    }, 
    {
        "name": "Музей имени Сурикова",
        "decription": """Отличный музей. Первое - компактный. За пол часа- час можно обойти все залы.
        Второе - расположен в очень красивом здании, построенном в стиле Модерн. И дом этот с историей.""",
        "logitude": 100.0,
        "latitude": 5.3423
    },
    {
        "name": "СибГУ им. Решетнёва",
        "description": """Окончил специалитет, аспирантуру и стал кандидатом наук! Всем желаю сделать правильный выбор""",
        "longitude": 54.0,
        "latitude": 200.0
    }
]


class TestForm(TestCase):
    """
        form validation test
    """

    def test_good_valid_form(self):
        """
        Check form validation works correctly for using good valid data
        """
        for data in GOOD_DATA_FOR_FORM:
            form = PlacesForm(data=data)
            self.assertTrue(form.is_valid())
    
    def test_bad_valid_form(self):
        """
        Check form validation works correctly for using bad valid data
        There are cases having blank fields and not unacceptable values
        """
        for data in BAD_DATA_FOR_FORM:
            form = PlacesForm(data=data)
            self.assertFalse(form.is_valid())

class TestGettingReviews(TestCase):
    """
        Getting list of reviews test
    """

    def setUp(self):
        self.client = Client()
        self.sign_up = reverse("login")

        def test_project_list_GET(self):
            response = self.client.get(reverse("main"))
            self.assertQuerysetEqual(response.context_data["reviews"],
                                     PlaceModel.objects.filter(user=self.client))