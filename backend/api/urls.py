from django.urls import path, include
from .views import SampleView

urlpatterns = [
    path('sample/', SampleView.as_view(), name='sample'),
    path('api/', include('api.urls')),
]
