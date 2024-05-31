from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news(request):
  news = Articles.objects.order_by('-date')
  return render(request, 'news/news.html', {'news': news})

class NewsDetailView(DetailView):
  model = Articles
  template_name = 'news/detail_view.html'
  context_object_name = 'article'

class NewsUpdateView(UpdateView):
  model = Articles
  template_name = 'news/create.html'
  form_class = ArticlesForm

class NewsDeleteView(DeleteView):
  model = Articles
  template_name = 'news/delete.html'
  success_url = '/news/'

def create(request):
  error = ''
  if request.method == 'POST':
    form = ArticlesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('news')
    else:
      error = 'Форма некорректно заполнена'
  form = ArticlesForm()

  date = {
    'form': form,
    'error': error
  }
  return render(request, 'news/create.html', date)
