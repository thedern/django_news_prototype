from django.urls import reverse_lazy
# A view that displays a form for creating an object, redisplaying the form with validation errors
# (if there are any) and saving the object.
from django.views.generic import CreateView

# Create your views here.
from .forms import CustomUserCreationForm


# signup view
class SignUpView(CreateView):
    """
    SignUpView subclasses CreateView and uses the custom form
    pass view to signup.html
    redirects to login page after signup
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
