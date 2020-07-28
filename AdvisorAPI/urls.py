from django.urls import path, include
from .views import AdminAdvisorView, AllAdvisorView, BookAdvisorView, AllBookedAdvisor
urlpatterns = [
    path('admin/advisor/', AdminAdvisorView.as_view()),
    path('advisor/', AllAdvisorView.as_view()),
    path('advisor/<int:AdvisorId>', BookAdvisorView.as_view()),
    path('advisor/<int:AdvisorId>/booking', AllBookedAdvisor.as_view()),
]