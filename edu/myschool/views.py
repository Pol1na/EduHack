from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.shortcuts import render, get_object_or_404, redirect, reverse


def profile(request, pk):
    if request.user.role_id == 1:
        user_role = get_object_or_404(Teacher, pk=pk)

        context = {'user_role': user_role}
        return render(request, 'profile.html', context=context)
    elif request.user.role_id == 2:
        user_role = get_object_or_404(Student, pk=pk)
        schedule = Schedule.objects.get(school_class=user_role.school_class)
        context = {'user_role': user_role, 'schedule': schedule}
        # тут надо починить
        return render(request, 'profile.html', context=context)

# class ProfileView(DetailView):
#     model = Teacher
#     template_name = 'profile.html'
#     context_object_name = 'item'
#
#     def get_context_data(self, *args, **kwargs):
#         cd = super().get_context_data(*args, **kwargs)
#
#         data = cartData(self.request)
#         cartItems = data['cartItems']
#         order = data['order']
#         items = data['items']
#
#         cd['data'] = data
#
#         return cd
