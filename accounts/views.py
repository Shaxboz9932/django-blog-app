from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    form_class = UserCreationForm
