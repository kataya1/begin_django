from django.urls import path, include
from accounts import views
app_name="accounts"
urlpatterns = [
    path('logout', views.logout, name="logout"),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.index, name='profile'),
]