from django.shortcuts import render

from ideas.forms import FileUploadForm2, CommentForm
from ideas.functions.user_function import whoLogged
from ideas.models import Report, Comment
from django.contrib import messages


def fileView(request):
    if request.method == 'POST':
        form = FileUploadForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dodano nowegy plik")
        else:
            messages.error(request, f"Niepoprawny plik")
    else:
        form = FileUploadForm2(request.POST, request.FILES)
    reports = Report.objects.all()
    logged = whoLogged(request)
    context = {
        'reports': reports,
        'form': form,
        'logged': logged
    }
    return render(request, 'registration/report/reports.html', context)


def comment(request, pk=None):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                id_report=Report.objects.get(id=pk),
                owner=request.user,
                content=request.POST['content']
            )
            comment.save()
            messages.success(request, f"Dodano komentarz")
    else:
        form = CommentForm()
    comment = Comment.objects.filter(id_report=pk)
    context = {
        'comments': comment,
        'form': form
    }
    return render(request, 'registration/report/comment.html', context)


