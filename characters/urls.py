from django.urls import path

from .views import HomePageView, AboutPageView, CharacterCreateView, CharacterUpdateView,\
    CharacterDeleteView, CharacterDetailView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('<int:pk>/', CharacterDetailView.as_view(), name='detail-view'),
    path('new/', CharacterCreateView.as_view(), name='create-view'),
    path('<int:pk>/delete', CharacterDeleteView.as_view(), name='delete-view'),
    path('<int:pk>/edit', CharacterUpdateView.as_view(), name='update-view')
]
