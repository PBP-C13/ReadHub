from django.shortcuts import render

# Create your views here.
def show_detail(request, id):
    context={

    }

    return render(request, "detail.html", context)
