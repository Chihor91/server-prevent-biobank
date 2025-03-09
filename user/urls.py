from django.urls import path

from .views import UserViewSet

urlpatterns = [
	path('all/', UserViewSet.as_view({'get' : 'list'}), name='get all users')
]