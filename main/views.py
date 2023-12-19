from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from book.models import Book
from main.models import PrivacyPolicy
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def show_main(request):
    products = Book.objects.filter(pk=2)

    context = {
        'name': request.user.username,
        'products': products
    }

    return render(request, "main.html", context)


def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autentikasi pengguna yang baru dibuat
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Login pengguna
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

def get_privacy_policy(request):
    privacy_policy = PrivacyPolicy.objects.first()
    if privacy_policy:
        data = {
            'privacy_policy': privacy_policy.content,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Privacy Policy not found'})
    

def privacy_policy(request):
    try:
        # Ganti dengan path yang sesuai tempat Anda menyimpan file
        with open('main/text/privacy_policy.txt', 'r') as file:
            privacy_policy_text = file.read()

        data = {'privacy_policy': privacy_policy_text}
        return JsonResponse(data)
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)