from django.contrib import admin
from .models import *


admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(SchoolClass)
admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(Parent)
admin.site.register(Homework)
admin.site.register(HomeworkForStudent)

