from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from .models import Gamers
from .forms import GamersForm
class AllGammers(ListView):
    template_name = 'list_gammers.html'
    model = Gamers

class MainPage(TemplateView):
    template_name = 'main_page.html'

class AddGammerViev(CreateView):
    template_name = 'create_user.html'
    model = Gamers
    form_class = GamersForm

    def get_success_url(self):
        return reverse('all')

class DeleteGammerView(DeleteView):

    model = Gamers
    success_url = reverse_lazy('all')
# Create your views here.
