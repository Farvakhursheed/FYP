from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_customer:
            return redirect('customers:home_content')
        else:
            return redirect('clients:home_content')
    return render(request, 'home.html')

def showDemoPage(request):
    return render(request,"demo.html")

#class homeView(TemplateView):
#    template_name = "home.html"