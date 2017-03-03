from django.forms import ModelForm
from demo.models import LibraryFine
class LibraryFineForm(ModelForm):

    class Meta:
        model = LibraryFine
        # fields = ['book_count', 'amount_fined',]
        fields = '__all__'

