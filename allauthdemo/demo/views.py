from django.shortcuts import render, get_object_or_404
# Create your views here.
#Library Fine list's view
from .models import LibraryFine

def fine_list(request):
    fines = LibraryFine.published.all()
    return render(request,)