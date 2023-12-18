from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', NewsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', NewsByTags.as_view(), name='tags'),
    path('news/<str:slug>/', GetNews.as_view(), name='news'),
    path('search/', Search.as_view(), name='search'),
]