from django.shortcuts import render
from .models import Test


def test_list(request):
    tests = Test.objects.all()
    return render(request, 'testapp/test_list.html', {'tests': tests})


def test(request):
    tests = Test.objects.all()
    return render(request, 'testapp/index.html', {'tests': tests})


# Create your views here.
