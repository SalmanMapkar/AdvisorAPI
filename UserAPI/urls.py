from django.urls import path, include
from .views import UserDataRegistration, UserDataView
urlpatterns = [
    path('register/', UserDataRegistration.as_view()),
    path('login/', UserDataView.as_view()),
    path('<int:UserId>/', include('AdvisorAPI.urls')),
]