from django.contrib.auth.models import User

from ideas.models import Local


def admin(request):
    local = Local.objects.all()
    admins = User.objects.all()
    for x in local:
        for y in admins:
            if x.admin == y:
                admin = y
                return admin