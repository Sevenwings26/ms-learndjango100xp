from django.urls import path
from . import views

urlpatterns = [
    path('', views.shelter_list, name='shelter_list'),
    path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail'),

    #TODO: Register Detail View
    path('dog<int:pk>', views.DogDetailView.as_view(), name='dog_detail'),
]