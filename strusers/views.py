from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from .models import Gamers
from .forms import GamersForm
class AllGammers(ListView):
    template_name = 'list_gammers.html'
    model = Gamers
    def get_context_data(self, **kwargs):
        con = super(AllGammers, self).get_context_data(**kwargs)
        con['g_count'] = len(self.object_list) + 2
        return con

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
