# from django import forms
# from django.forms import ModelForm
# from .models import Library

# class LibraryForm(ModelForm):
#     class Meta:
#         model = Library
        
#         fields = ('book_title', 'book_author', 'book_pages')

#         widgets = {
#             'book_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book_Name'}),
#             'book_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
#             'book_pages': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pages'}),
            
#         }