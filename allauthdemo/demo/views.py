from django.shortcuts import render, get_object_or_404
# Create your views here.
#Library Fine list's view
from .models import LibraryFine
from .forms import LibraryFineForm
# def fine_list(request):
#     fines = LibraryFine.published.all()
#     return render(request,)



@login_required
def library_fine_new(request):
    t = loader.get_template('libraryfine/library-fine.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')


@login_required
def shahparan_hall_new(request):
    t = loader.get_template('hall/hall.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')
@login_required
def transcript_new(request):
    t = loader.get_template('libraryfine/library-fine.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')


@login_required
def certificate_new(request):
    t = loader.get_template('libraryfine/library-fine.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')
@login_required
def cash_memo_new(request):
    t = loader.get_template('libraryfine/library-fine.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')


@login_required
def STD_2_new(request):
    t = loader.get_template('libraryfine/library-fine.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')
@login_required
def STD_6_new(request):
    t = loader.get_template('libraryfine/library-fine.html')
    c = {}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')
