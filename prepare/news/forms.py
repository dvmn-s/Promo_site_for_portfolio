from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title',  'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of article'
                }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Full_text'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publication'
            }),



        }

