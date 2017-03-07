from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LibraryFine
from forms import *
from django.shortcuts import redirect


@login_required
def library_fine_new(request):
    if request.method == "POST":
        form = LibraryFineForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('library_fine_print',pk = post.pk)
    else:
        form = LibraryFineForm()
   
    return render(request,'libraryfine/library-fine.html',{'form':form})

@login_required
def library_fine_print(request, pk):
    post = get_object_or_404(LibraryFine, pk=pk)
    return render(request, 'libraryfine/library-fine-print.html',{'post':post})

@login_required
def shahparan_hall_new(request):
    if request.method == "POST":
            form = ShahparanHallForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect('shahparan_hall_print', pk = post.pk)
    else:
        form = ShahparanHallForm()
   
    return render(request,'hall/hall.html',{'form':form})
@login_required
def shahparan_hall_print(request, pk):
    post = get_object_or_404(ShahparanHall, pk=pk)
    return render(request,'hall/shahparan-hall-print.html',{'post':post})


@login_required
def transcript_new(request):
    if request.method == "POST":
            form = TranscriptForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect('transcript_print',pk=post.pk)
    else:
        form = TranscriptForm()
   
    return render(request,'registrar/transcript.html',{'form':form})

@login_required
def transcript_print(request, pk):
    post = get_object_or_404(Transcript, pk=pk)
    return render(request, 'registrar/transcript-print.html',{'post':post})
@login_required
def gradesheet_new(request):
    if request.method == "POST":
            form = GradesheeteForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect(request, 'gradesheet_print', pk=post.pk)
    else:
        form = GradesheeteForm()
    return render(request,'registrar/gradesheet.html',{'form':form})
@login_required
def gradesheet_print(request, pk):
    post = get_object_or_404(Gradesheet, pk=pk)
    return render(request, 'registrar/gradesheet-print.html',{'post':post})

@login_required
def cash_memo_new(request):
    if request.method == "POST":
            form = CashMemoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect(request, 'cashmemo_print', pk=post.pk)
                
    else:
        form = CashMemoForm()
    return render(request,'bank/cashmemo.html',{'form':form})


@login_required
def cashmemo_print(request, pk):
    post = get_object_or_404(CashMemo, pk=pk)
    return render(request, 'bank/cashmemo-print.html',{'post':post})
@login_required
def S_2_new(request):
    if request.method == "POST":
            form = S2Form(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect(request, 's2_print', pk=post.pk)
    else:
        form = S2Form()
    return render(request,'bank/s2.html',{'form':form})
@login_required
def s2_print(request, pk):
    post = get_object_or_404(CashMemo, pk=pk)
    return render(request, 'bank/s2-print.html',{'post':post})
@login_required
def STD_6_new(request):
    if request.method == "POST":
            form = STD6Form(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect(request, 'std6_print', pk=post.pk)
    else:
        form = STD6Form()
    return render(request,'bank/std6.html',{'form':form})

@login_required
def std6_print(request, pk):
    post = get_object_or_404(CashMemo, pk=pk)
    return render(request, 'bank/std6-print.html',{'post':post})