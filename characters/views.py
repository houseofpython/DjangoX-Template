from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Character
from django.urls import reverse_lazy


class HomePageView(ListView):
    template_name = "characters/home.html"
    model = Character
    context_object_name = 'characters'


class AboutPageView(ListView):
    template_name = "characters/about.html"
    model = Character


class CharacterDetailView(DetailView):
    template_name = 'characters/char-detail.html'
    model = Character


class CharacterCreateView(CreateView):
    template_name = 'characters/char-create.html'
    model = Character
    fields = ['name', 'description', 'house']


class CharacterUpdateView(UpdateView):
    template_name = 'characters/char-update.html'
    model = Character
    fields = ['name', 'description', 'house']


class CharacterDeleteView(DeleteView):
    template_name = 'characters/char-delete.html'
    model = Character
    success_url = reverse_lazy('home')


