from django.urls import path
from . import views


urlpatterns=[
    path('payment/', views.OrderApiView.as_view()),
    path('get-status/<str:id>',views.OrderApiView.as_view()),
]
