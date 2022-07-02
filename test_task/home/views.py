from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from rest_framework import generics
from home.forms import LoginUserForm
from home.models import TelegramUser
from home.serializers import TelegramUserSerializer


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')

        return render(self.request, 'home/login.html', {'form': self.form_class})

    def get_success_url(self):
        return reverse_lazy('home')


class Home(ListView):
    model = TelegramUser
    template_name = 'home/home.html'
    context_object_name = 'tg_user'

    def get_queryset(self):
        return self.model.objects.get(site_user__id=self.request.user.id)


def logout_user(request):
    logout(request)
    return redirect('login')


class TelegramUserViewSet(generics.CreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer

