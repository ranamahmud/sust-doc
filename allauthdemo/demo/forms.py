from django import forms
from .models import *
class LibraryFineForm(forms.ModelForm):

    class Meta:
        model = LibraryFine
        fields = '__all__'


class ShahparanHallForm(forms.ModelForm):

    class Meta:
        model = ShahparanHall
        fields = '__all__'
class TranscriptForm(forms.ModelForm):
    
    class Meta:
        model = Transcript
        fields = '__all__'
class CertificateForm(forms.ModelForm):
    
    class Meta:
        model = Certificate
        fields = '__all__'
class CashMemoForm(forms.ModelForm):
    
    class Meta:
        model = CashMemo
        fields = '__all__'
class STD2Form(forms.ModelForm):
    
    class Meta:
        model = STD2
        fields = '__all__'
class STD6Form(forms.ModelForm):
    
    class Meta:
        model = STD6
        fields = '__all__'