from django import forms
from .models import LibraryFine
class LibraryFineForm(forms.ModelForm):

    class Meta:
        model = LibraryFine
        # fields = ['book_count', 'amount_fined',]
        fields = '__all__'

