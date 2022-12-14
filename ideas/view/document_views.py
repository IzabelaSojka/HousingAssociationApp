from django.shortcuts import render

from ideas.forms import FileUploadForm2
from ideas.functions.user_function import whoLogged
from ideas.models import Report
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
