from django.forms import ModelForm
from .models import BorrowedBook

class BorrowForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['borrow_duration', 'terms_accepted_1', 'terms_accepted_2', 'terms_accepted_3']