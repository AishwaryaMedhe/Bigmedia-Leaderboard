
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import MediaOutlet, Article


# Media Outlet Views
class MediaOutletListView(ListView):
    model = MediaOutlet
    template_name = 'MediaApp/media_outlet_list.html'
    context_object_name = 'outlets'
    paginate_by = 10
    ordering = ['name']


class MediaOutletDetailView(DetailView):
    model = MediaOutlet
    template_name = 'MediaApp/media_outlet_detail.html'
    context_object_name = 'outlet'


class MediaOutletCreateView(CreateView):
    model = MediaOutlet
    template_name = 'MediaApp/media_outlet_form.html'
    fields = ['name', 'score']
    success_url = reverse_lazy('media_outlet_list')

    def form_valid(self, form):
        messages.success(self.request, 'Media outlet created successfully!')
        return super().form_valid(form)


class MediaOutletUpdateView(UpdateView):
    model = MediaOutlet
    template_name = 'MediaApp/media_outlet_form.html'
    fields = ['name', 'score']
    context_object_name = 'outlet'

    def get_success_url(self):
        return reverse_lazy('media_outlet_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Media outlet updated successfully!')
        return super().form_valid(form)


class MediaOutletDeleteView(DeleteView):
    model = MediaOutlet
    template_name = 'MediaApp/media_outlet_confirm_delete.html'
    context_object_name = 'outlet'
    success_url = reverse_lazy('media_outlet_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Media outlet deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Article Views
class ArticleListView(ListView):
    model = Article
    template_name = 'MediaApp/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'MediaApp/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'MediaApp/article_form.html'
    fields = ['title', 'url', 'outlet', 'shares', 'views']
    success_url = reverse_lazy('article_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outlets'] = MediaOutlet.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Article created successfully!')
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'MediaApp/article_form.html'
    fields = ['title', 'url', 'outlet', 'shares', 'views']
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outlets'] = MediaOutlet.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Article updated successfully!')
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'MediaApp/article_confirm_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Article deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Function-based alternatives if preferred
# Media Outlet function views
# def media_outlet_list(request):
#     outlets = MediaOutlet.objects.all().order_by('name')
#     return render(request, 'media_outlet_list.html', {'outlets': outlets})
#
#
# def media_outlet_detail(request, pk):
#     outlet = get_object_or_404(MediaOutlet, pk=pk)
#     return render(request, 'media_outlet_detail.html', {'outlet': outlet})
#
#
# def media_outlet_create(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         score = request.POST.get('score', 0)
#
#         outlet = MediaOutlet.objects.create(
#             name=name,
#             score=score
#         )
#
#         messages.success(request, 'Media outlet created successfully!')
#         return redirect('media_outlet_detail', pk=outlet.pk)
#
#     return render(request, 'media_outlet_form.html')
#
#
# def media_outlet_update(request, pk):
#     outlet = get_object_or_404(MediaOutlet, pk=pk)
#
#     if request.method == 'POST':
#         outlet.name = request.POST.get('name')
#         outlet.score = request.POST.get('score', 0)
#         outlet.save()
#
#         messages.success(request, 'Media outlet updated successfully!')
#         return redirect('media_outlet_detail', pk=outlet.pk)
#
#     return render(request, 'media_outlet_form.html', {'outlet': outlet})
#
#
# def media_outlet_delete(request, pk):
#     outlet = get_object_or_404(MediaOutlet, pk=pk)
#
#     if request.method == 'POST':
#         outlet.delete()
#         messages.success(request, 'Media outlet deleted successfully!')
#         return redirect('media_outlet_list')
#
#     return render(request, 'media_outlet_confirm_delete.html', {'outlet': outlet})
#
#
# # Article function views
# def article_list(request):
#     articles = Article.objects.all().order_by('-created_at')
#     return render(request, 'article_list.html', {'articles': articles})
#
#
# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'article_detail.html', {'article': article})
#
#
# def article_create(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         url = request.POST.get('url')
#         outlet_id = request.POST.get('outlet')
#         shares = request.POST.get('shares', 0)
#         views = request.POST.get('views', 0)
#
#         outlet = get_object_or_404(MediaOutlet, pk=outlet_id)
#
#         article = Article.objects.create(
#             title=title,
#             url=url,
#             outlet=outlet,
#             shares=shares,
#             views=views
#         )
#
#         messages.success(request, 'Article created successfully!')
#         return redirect('article_detail', pk=article.pk)
#
#     outlets = MediaOutlet.objects.all()
#     return render(request, 'article_form.html', {'outlets': outlets})
#
#
# def article_update(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#
#     if request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.url = request.POST.get('url')
#         outlet_id = request.POST.get('outlet')
#         article.outlet = get_object_or_404(MediaOutlet, pk=outlet_id)
#         article.shares = request.POST.get('shares', 0)
#         article.views = request.POST.get('views', 0)
#         article.save()
#
#         messages.success(request, 'Article updated successfully!')
#         return redirect('article_detail', pk=article.pk)
#
#     outlets = MediaOutlet.objects.all()
#     return render(request, 'article_form.html', {'article': article, 'outlets': outlets})
#
#
# def article_delete(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#
#     if request.method == 'POST':
#         article.delete()
#         messages.success(request, 'Article deleted successfully!')
#         return redirect('article_list')
#
#     return render(request, 'article_confirm_delete.html', {'article': article})

