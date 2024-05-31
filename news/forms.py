from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
  class Meta:
    model = Articles
    fields = ['title', 'anons', 'text', 'date']

    widgets = {
      'title': TextInput(attrs={
        'placeholder': "Название статьи",
			  'class': "form-control"
      }),
      'anons': TextInput(attrs={
        'placeholder': "Анонс статьи",
			  'class': "form-control"
      }),
      'text': Textarea(attrs={
        'placeholder': "Текст статьи",
			  'class': "form-control"
      }),
      'date': DateTimeInput(attrs={
        'placeholder': "Дата публикации",
			  'class': "form-control"
      }),

    }