from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm


# Register view
class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


