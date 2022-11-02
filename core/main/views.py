from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Phone, NoteBook

# Create your views here.

class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class PhoneListView(ListView):
    template_name = 'phone.html'

    def get(self, request):
        phones = Phone.objects.all()
        return render(request, self.template_name, {'phones': phones})

class PhoneDetailView(DetailView):
    template_name = 'phone_details.html'

    def get(self, request, slug):
        phone = Phone.objects.get(slug=slug)
        return render(request, self.template_name, {'phone': phone})

class NoteBookListView(ListView):
    template_name = 'notebook.html'

    def get(self, request):
        notebooks = NoteBook.objects.all()
        return render(request, self.template_name, {'notebooks': notebooks})

class NoteBookDetailView(DetailView):
    template_name = 'notebook_detail.html'

    def get(self, request, slug):
        notebook = NoteBook.objects.get(slug=slug)
        return render(request, self.template_name, {'notebook': notebook})
