from django import forms
from .models import *
class LibraryFineForm(forms.ModelForm):

    class Meta:
        model = LibraryFine
        # fields = '__all__'
        fields = ['date','gender','book_count','amount_fined']



class ShahparanHallForm(forms.ModelForm):

    class Meta:
        model = ShahparanHall
        fields = '__all__'
        exclude = ['user']
class TranscriptForm(forms.ModelForm):
    
    class Meta:
        model = Transcript
        fields = '__all__'
        exclude = ['user']
class GradesheeteForm(forms.ModelForm):
    
    class Meta:
        model = Gradesheet
        fields = '__all__'
        exclude = ['user']
class CashMemoForm(forms.ModelForm):
    
    class Meta:
        model = CashMemo
        fields = '__all__'
        exclude = ['user']
class S2Form(forms.ModelForm):
    
    class Meta:
        model = S2
        fields = '__all__'
        exclude = ['user']
class STD6Form(forms.ModelForm):
    
    class Meta:
        model = STD6
        fields = '__all__'
        exclude = ['user']