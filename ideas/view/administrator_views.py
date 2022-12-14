from django.shortcuts import render

from ideas.functions.administrator_function import admin


def adminEmail(request):
    adminElement = admin(request)
    context = {
        'admin': adminElement
    }
    return render(request, 'registration/administrator/admin_email.html', context)

def administrator(request):
    adminElement = admin(request)
    context = {
        'admin': adminElement
    }
    return render(request, 'registration/administrator/admin_profile.html', context)
