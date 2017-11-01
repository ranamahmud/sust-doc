from django import forms
from .models import *
class LibraryFineForm(forms.ModelForm):

    class Meta:
        model = LibraryFine
        # fields = '__all__'
        fields = ['date','gender','book_count','amount_fined']
        widgets = {'date': forms.DateInput()}


class ShahparanHallForm(forms.ModelForm):
   
    class Meta:
        model = ShahparanHall
        fields = '__all__'
        exclude = ['user','created_date','published_date']
        widgets = {'date': forms.DateInput()}
        
        
class TranscriptForm(forms.ModelForm):
    
    class Meta:
        model = Transcript
        fields = '__all__'
        exclude = ['user','created_date','published_date']
        widgets = {'date': forms.DateInput()}
class GradesheeteForm(forms.ModelForm):
    
    class Meta:
        model = Gradesheet
        fields = '__all__'
        exclude = ['user','created_date','published_date']
        widgets = {'date': forms.DateInput()}
class CashMemoForm(forms.ModelForm):
    
    class Meta:
        model = CashMemo
        fields = '__all__'
        exclude = ['user','created_date','published_date']
        widgets = {'date': forms.DateInput()}  
class S2Form(forms.ModelForm):
    
    class Meta:
        model = S2
        fields = '__all__'
        exclude = ['user','created_date','published_date']
        widgets = {'date': forms.DateInput()}
class STD6Form(forms.ModelForm):
    
    class Meta:
        model = STD6
        fields = '__all__'
        exclude = ['user','created_date','published_date']
        widgets = {'date': forms.DateInput()}