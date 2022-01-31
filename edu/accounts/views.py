from django.shortcuts import render
# from .forms import LoginForm, UserRegistrationForm
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate  # add this
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password1'])
            login(request, user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form})


# #
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')

#
# def login(request):
#     return render(request, 'news/login.html')
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password1'])
#             # Save the User object
#             new_user.save()
#             return redirect('login')
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'register.html', {'user_form': user_form})
