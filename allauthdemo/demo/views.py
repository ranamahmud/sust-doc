from django.shortcuts import render, get_object_or_404
# Create your views here.
#Library Fine list's view
from .models import LibraryFine
from .forms import LibraryFineForm
# def fine_list(request):
#     fines = LibraryFine.published.all()
#     return render(request,)

def library_fine_new():
    form = LibraryFineForm()
    return render(request,'')

@login_required
def library_fine_new(request):
    t = loader.get_template('libraryfine/library-fine.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')