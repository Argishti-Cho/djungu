from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('phones/', PhoneListView.as_view(), name='phone'),
    path('phones/<str:slug>/', PhoneDetailView.as_view(), name='phone_details'),
    path('notebooks/', NoteBookListView.as_view(), name='notebook'),
    path('notebooks/<str:slug>/', NoteBookDetailView.as_view(), name='notebook_detail'),
]