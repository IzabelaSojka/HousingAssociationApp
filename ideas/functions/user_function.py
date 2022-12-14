from ideas.models import Local


def whoLogged(request):
    locals = Local.objects.all()
    logged = 'nobody'
    for local in locals:
        if local.admin == request.user:
            logged = 'admin'
            break
        elif local.owner == request.user:
            logged = 'resident'
            break
    return logged
