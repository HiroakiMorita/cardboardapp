from django.urls import path, include
from rest_framework import routers
from . import views
from .views import UserViewSet

app_name = 'cardboardapp'


router = routers.SimpleRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='users_detail'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='users_update'),
    path('predict/', views.predict, name='predict'),
]