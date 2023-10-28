from django.forms import ModelForm
from favorit.models import favorit


class FavoritForm(ModelForm):
    class Meta:
        model = favorit
        fields = ["books"]