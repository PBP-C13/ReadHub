from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from detail.models import Detail
from book.models import Book
import random, json
from django.core import serializers
from django.http import JsonResponse
from detail.forms import DetailForm
from django.core.exceptions import PermissionDenied


from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def show_detail(request):
    details = Detail.objects.all()  # Retrieve all detail objects from the database
    all_books = Book.objects.all()[:100]

    context = {
        'books': all_books,
        'name': request.user.username
    }
    return render(request, "detail.html", context)

def borrow_flow(request):
    # You can add view logic here
    return render(request, 'borrow_flow.html')

def get_item_json(request):
    all_books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', all_books))

def get_book_details(request):
    # Load book data from the JSON file
    with open('book/fixture/book.json', 'r') as json_file:
        book_data = json.load(json_file)

    return JsonResponse(book_data)

@csrf_exempt
def create_review(request): # submit feedback
    if(request.method == "POST" ):
        form = DetailForm(request.POST)
        if(form.is_valid):
            # form.instance.user = request.user
            formSave = form.save()
            return JsonResponse({
                "data": form.data,
                "id": formSave.id,
            })

        return JsonResponse({"data": {
            # "user": request.user,
            # "username": request.user.name
        }})
    else:       
        raise PermissionDenied("Anda bukan pasien!")

