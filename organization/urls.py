from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, EmploymentHistoryViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'employment-history', EmploymentHistoryViewSet, basename='employment-history')

urlpatterns = [
    path('api/', include(router.urls)),
]
