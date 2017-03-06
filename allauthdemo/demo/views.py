from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LibraryFine
from forms import *



@login_required
def library_fine_new(request):
    if request.method == "POST":
        form = LibraryFineForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
    else:
        form = LibraryFineForm()
   
    return render(request,'libraryfine/library-fine.html',{'form':form})



@login_required
def shahparan_hall_new(request):
    if request.method == "POST":
            form = ShahparanHallForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
    else:
        form = ShahparanHallForm()
   
    return render(request,'hall/hall.html',{'form':form})



@login_required
def transcript_new(request):
    if request.method == "POST":
            form = TranscriptForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
    else:
        form = TranscriptForm()
   
    return render(request,'registrar/transcript.html',{'form':form})


@login_required
def certificate_new(request):
    if request.method == "POST":
            form = CertificateForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
    else:
        form = CertificateForm()
    return render(request,'registrar/certificate.html',{'form':form})

@login_required
def cash_memo_new(request):
    if request.method == "POST":
            form = CashMemoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
    else:
        form = CashMemoForm()
    return render(request,'bank/cashmemo.html',{'form':form})


@login_required
def S_2_new(request):
    if request.method == "POST":
            form = S2Form(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
    else:
        form = S2Form()
    return render(request,'bank/std2.html',{'form':form})

@login_required
def STD_6_new(request):
    if request.method == "POST":
            form = STD6Form(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
    else:
        form = STD6Form()
    return render(request,'bank/std6.html',{'form':form})

