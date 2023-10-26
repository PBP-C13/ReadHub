from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from detail.forms import DetailForm
from detail.models import Detail
from book.models import Book

def show_detail(request):
    details = Detail.objects.all()
    all_books = Book.objects.all()[:100]
    context = {
        'books': all_books,
        'name': request.user.username if request.user.is_authenticated else "Guest",
    }
    return render(request, "detail.html", context)

def borrow_flow(request):
    # Add view logic for the borrow flow here
    return render(request, 'borrow_flow.html')

def get_item_json(request):
    all_books = Book.objects.all()
    data = serializers.serialize('json', all_books)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def create_review(request):
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user if request.user.is_authenticated else None
            form_save = form.save()
            return JsonResponse({
                "success": True,
                "message": "Review created successfully",
                "review_id": form_save.id,
            })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid form data",
            })
    else:
        return JsonResponse({
            "success": False,
            "message": "Invalid request method",
        })
