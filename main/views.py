from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def login_user(request):
    return render(request, 'auth/login-register.html')

# from django.shortcuts import render
# from authentication.forms import LoginForm
#
#
# def index(request):
#     return render(request, 'index.html')
#
#
# def about(request):
#     return render(request, 'about-us.html')
#
#
# def login_user(request):
#     context = {'login_form': LoginForm()}
#     return render(request, 'login-register.html', context)