from django.views.generic import TemplateView, CreateView
from . import forms
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'phone/home.html'

class AddPhoneFormView(CreateView):
    template_name = 'phone/add_persone.html'
    from_class = forms.CreatePersoneFrom
