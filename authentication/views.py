

from django.contrib.auth import logout, login, authenticate

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from authentication.forms import LoginForm, RegisterForm


def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('login_user')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'The user with username {username} and password was not found!'
                }

    return render(request, 'auth/login.html', context)


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return render(request, 'auth/login-register.html', {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'auth/login-register.html', {'user_form': user_form})


class RegisterView(TemplateView):
    template_name = 'auth/registration.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'auth/registration.html', context)

    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('index')

        context = {'user_form': user_form}
        return render(request, 'auth/registration.html', context)



# def login_register(request):
#     context = {'login_form': LoginForm()}
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('index')
#             else:
#                 context = {
#                     'login_form': login_form,
#                     'attention': f'The user with username {username} and password was not found!'
#                 }
#
#
#     return render(request, 'auth/login-register.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')


# def login_user(request):
#     context = {'login_form': LoginForm()}
#     return render(request, 'login-register.html', context)
