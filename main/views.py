
from django.shortcuts import render, get_object_or_404
from .models import Tour
from .forms import TourForm, TourRegisterForm
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.views import generic


class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'tour_detail.html'
    context_object_name = "tour"


class TourRegisterView(generic.UpdateView):
    model = CustomUser     
    form_class = TourRegisterForm
    template_name = 'tour_register.html'
    # context_object_name = "tour"    
    success_url = reverse_lazy('home')


class TourListView(generic.ListView):
    model = Tour
    template_name = 'tour_list.html'
    context_object_name = 'tours'


def home(request):
    return render(request, 'home.html')