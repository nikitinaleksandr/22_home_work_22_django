from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from blog.models import Blog


class BlogBaseView(TemplateView):
    template_name = 'blog/base.html'


class BlogListView(ListView):
    model = Blog


    def get_queryset(self):
        return Blog.objects.filter(is_published=True)  # только опубликованные



class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count +=1
        self.object.save()
        return self.object



class BlogCreateView(CreateView):
    model = Blog
    fields = ("name", "description", "image", "is_published", "views_count")

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("name", "description", "image", "is_published", "views_count")

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


