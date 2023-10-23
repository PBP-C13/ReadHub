from django.forms import ModelForm
from main.models import Forum

class ProductForm(ModelForm):
    class Meta:
        model = Forum
        fields = ["pesan"]