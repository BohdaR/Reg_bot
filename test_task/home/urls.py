from django.urls import path, include
from home.views import LoginUser, logout_user, TelegramUserViewSet, Home

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', Home.as_view(), name='home'),
    path('api/v1/telegram/users/', TelegramUserViewSet.as_view()),
    path('api/v1/auth/', include('djoser.urls'))
]

