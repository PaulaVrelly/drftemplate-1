from django.urls import path

from crud.views import (
    RetrievePersonsAPIView,
    CreatePersonAPIView, 
    RetrieveUpdateDeletePersonAPIView,
    RetrieveRols,
    CreateRols,
    RetrieveUsers,
    CreateUsers)

urlpatterns = [
    path('list/', RetrievePersonsAPIView.as_view()),
    path('create/', CreatePersonAPIView.as_view()),
    path('<int:person_id>/', RetrieveUpdateDeletePersonAPIView.as_view()),
    path('roles/', RetrieveRols.as_view()),
    path('roles/create/', CreateRols.as_view()),
    path('users/', RetrieveUsers.as_view()),
    path('users/create/', CreateUsers.as_view())
]