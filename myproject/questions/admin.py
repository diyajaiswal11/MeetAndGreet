from django.contrib import admin

from .models import Question

#admin.site.register(Question)
#admin.site.register(Comment)
# Register your models here.
myModels = [Question]  # iterable list
admin.site.register(myModels)