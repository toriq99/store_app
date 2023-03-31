from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.

class LoginPage(View):

    def get(self, request):
        return render (request, "login/login.html")

    def post(self, request):
        pass
    