from django.urls import path
from .views import HomePageView, AboutPageView, InfoPageView, AdditiomPageView, IndexPageView
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('info/',InfoPageView.as_view(),name='info'),
    path('addition/',AdditiomPageView.as_view(),name='addition'),
    path('index/',IndexPageView.as_view(),name='index')
]