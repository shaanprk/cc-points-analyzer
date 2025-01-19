from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('verify/<int:user_id>/', VerifyEmailView.as_view(), name='verify_email')
]
