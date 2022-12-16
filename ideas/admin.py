from django.contrib import admin
from .models import Local, Billing, Report, Comment

admin.site.register(Local)
admin.site.register(Billing)
admin.site.register(Report)
admin.site.register(Comment)
