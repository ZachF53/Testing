from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings


from .forms import ContactForm, QuoteForm
from portfolio.models import Portfolio, Services, Additional

def index(request):
    form = QuoteForm()
    context = {
        'title': 'Home',
        "form": form
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            'Free Quote Request Form', 
            'Here is the message ' + message + ' You can contact me back at: ' + email, 
            'football45353@gmail.com', 
            ['football45353@gmail.com'], 
            fail_silently=False
        )

        return render(request, 'portfolio/thanks.html')
    return render(request, 'portfolio/index.html', context)

def portfolio(request):
    portfolio = Portfolio
    context = {
        'title': 'Portfolio',
        'portfolio': portfolio.objects.all()
    }
    return render(request, 'portfolio/portfolio.html', context)

def service(request):
    service = Services
    additional = Additional
    context = {
        'title': 'services',
        'service': service.objects.all(),
        'additional': additional.objects.all()
    }
    return render(request, 'portfolio/service.html', context)

def contact(request):
    form = ContactForm()
    context = {
        'title': 'Contact Me',
        "form": form
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        service = request.POST.get("service")
        message = request.POST.get("message")

        send_mail(
            'Contact Form', 
            'Here is the message ' + message + ' You can contact me back at: ' + email, 
            'football45353@gmail.com', 
            ['football45353@gmail.com'], 
            fail_silently=False
        )

        return render(request, 'portfolio/thanks.html')

    return render(request, 'portfolio/contact.html', context)

def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'portfolio/login.html', context)

def thanks(request):
    context = {
        'title': 'Thank You',
    }
    return render(request, 'portfolio/thanks.html', context)