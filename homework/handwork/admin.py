from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Student)
class Student_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender')
    ordering = ('id',)


@admin.register(models.Course)
class Course_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher')
    ordering = ('id',)


@admin.register(models.Score)
class Score_Admin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'number')


@admin.register(models.Teacher)
class Teacher_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')

    # def __str__(self):
    #     return "<Teacher: %s>" % self.title
