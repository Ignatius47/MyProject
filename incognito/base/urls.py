from django.urls import path
from . import views

# from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('endpoints/', views.endpoints, name='endpoints'),
    path('advocates/', views.advocate_list, name='advocate_list'),
    path('advocates/<str:username>/', views.advocate_detail, name='advocate_detail'),
    path('companies/', views.Companies_list, name='companies_list'),
]
