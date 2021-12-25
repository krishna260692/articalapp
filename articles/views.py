from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class Blogcreateview(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'post_new.html'
    fields = ('title','body')
    login_url = 'login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






class Deatilview(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'indiv_post'
    login_url = 'login'


class Editblog(LoginRequiredMixin,UpdateView):
    model = Article
    template_name = 'edit.html'
    fields = '__all__'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class Deleteblog(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



