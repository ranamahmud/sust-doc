from django import forms
from .models import LibraryFine
class LibraryFineForm(forms.Form):


    class Meta:
        model = LibraryFine
        fields = ('user','book_count')
        