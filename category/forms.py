from django.forms import ModelForm
from category.models import Category


class FavoritForm(ModelForm):
    class Meta:
        model = Category
        fields = ["books", "is_favorite"]