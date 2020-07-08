# A page representing a list of objects.
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    # object passed to the template
    model = Article
    template_name = 'article_list.html'
    # redirect to login for non-authenticated users
    login_url = 'login'

    # return only objects for the current user
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    # object passed to the template
    model = Article
    # optional context name passed to template
    context_object_name = "my_article"
    template_name = 'article_detail.html'
    # redirect to login for non-authenticated users
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # object passed to the template
    model = Article
    # editable fields
    fields = ('title', 'body', 'show')
    template_name = 'article_edit.html'
    # UpdateView automatically redirects to detail view unless success URL is added to the view
    # success_url = reverse_lazy('article_list')
    # redirect to login for non-authenticated users
    login_url = 'login'

    # restrict updating to author/owner
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # object passed to the template
    model = Article
    template_name = 'article_delete.html'
    # redirect upon delete
    success_url = reverse_lazy('article_list')
    # redirect to login for non-authenticated users
    login_url = 'login'

    # restrict updating to author/owner
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'body', 'show')
    template_name = 'article_new.html'
    # redirect to login for non-authenticated users
    login_url = 'login'

    # restrict author to authenticated user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



