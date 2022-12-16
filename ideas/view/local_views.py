from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ideas.forms import LocalForm
from ideas.models import Local
from django.contrib import messages


def local(request):
    if request.method == "POST":
        form = LocalForm(request.POST)
        if form.is_valid():
            local = Local(
                admin=request.user,
                owner=User.objects.get(id=request.POST["owner"]),
                number=request.POST['number'],
                area=request.POST['area']
            )
            local.save()
            messages.success(request, f"Lokal został dodany")
    else:
        form = LocalForm()
    local = Local.objects.filter(admin=request.user)
    context = {
        'locals': local,
        'form': form,
    }
    return render(request, 'registration/local/local.html', context)


def local_delete(request, pk = None):
    Local.objects.get(id=pk).delete()
    return redirect("local")
