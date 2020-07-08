# Renders a given template, with the context containing parameters captured in the URL.
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
