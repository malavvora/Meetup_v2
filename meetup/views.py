# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, CreateView, FormView, DetailView
from django.contrib.auth import authenticate, login, logout, forms
from meetup.forms import SignUpForm, CreateMeetupForm, LoginForm
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Category, Meetup, Group, User


class IndexPageView(TemplateView):
    template_name = 'index.html'
    category_list = Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['categories'] = self.category_list
        return context


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/profile/'
    template_name = 'registration/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


# class LoginView(FormView):
#     form_class = LoginForm
#     success_url = reverse_lazy('')
#     template_name = 'registration/login.html'
#
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             form = forms.AuthenticationForm(data=request.POST)
#             if form.is_valid():
#                 user = form.get_user()
#                 login(request, user)
#                 return HttpResponseRedirect("/profile/")
#         else:
#             form = forms.AuthenticationForm()
#         return render(request, 'registration/login.html', {'form': form})


class RegisterPage(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                raw_password = form.cleaned_data['password1']
                m = User(username=username, email=email,
                         password=raw_password, is_staff=True)
                m.save()
                login(request, m)
                return HttpResponseRedirect("/profile/")

        else:
            form = SignUpForm()

        return render(request, 'register.html', {'form': form})


class GroupView(DetailView):
    model = Category
    template_name = 'group.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        context['group_list'] = Group.objects.all()
        return context


class CreateMeetup(CreateView):
    form_class = CreateMeetupForm
    template_name = "create_meetup.html"
    cat = Category.objects.all()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CreateMeetupForm(request.POST)
            if form.is_valid():
                group = form.cleaned_data['meetup_group']
                place = form.cleaned_data['meetup_place']
                date = form.cleaned_data['meetup_date']
                m = Meetup(meetup_group=group, meetup_place=place,
                           meetup_date=date)
                m.save()
                return HttpResponse("Meetup created successfully")

        else:
            form = CreateMeetupForm()

        return render(request, 'create_meetup.html', {'form': form})


class UserProfileView(TemplateView):
    template_name = 'profile.html'
    groups_list = Group.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['groups'] = self.groups_list
        return context


class GroupDetails(DetailView):
    model = Group
    template_name = 'group_details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupDetails, self).get_context_data(**kwargs)
        context['meetup_list'] = Meetup.objects.all()
        return context

