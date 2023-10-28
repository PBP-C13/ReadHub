from django.forms import ModelForm
from .models import BorrowedBook

class BorrowForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['borrow_duration', 'terms_accepted']

# class ReturnForm(ModelForm):
#     class Meta:
#         model = BorrowedBook
#         fields = ['rating', 'review']