
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomCreateForm


class SignUpView(CreateView):
    form_class = CustomCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
