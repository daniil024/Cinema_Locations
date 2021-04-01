from django.contrib import admin

from .models import *

admin.site.register(Manager)
admin.site.register(Producer)
admin.site.register(Service)
admin.site.register(Tag)
admin.site.register(Ordering)
admin.site.register(Message)
