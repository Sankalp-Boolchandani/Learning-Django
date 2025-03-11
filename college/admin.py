from django.contrib import admin
from .models import *
from django.db.models import Sum
# Register your models here.

admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject)


# used to display data in the admin panel as passed in the list display since normally we only see the object name for all the models 
# this way we can view in the admin panel all the required params of the object
# also after creating this class, need to pass it as an extra param for the model this change is applied to!
# here it is for SubjectMarks and hence passed with registration of the model!!! 
class SubjectsMarksAdmin(admin.ModelAdmin):
  list_display=['student', 'subject', 'marks']  

admin.site.register(SubjectMarks, SubjectsMarksAdmin)


class ReportDisplay(admin.ModelAdmin):
  list_display=['student', 'diaplayTotalMarks', 'rank']
  ordering=['rank']
  def diaplayTotalMarks(self, obj):
    all_subs=SubjectMarks.objects.filter(student=obj.student)
    marks=all_subs.aggregate(marks=Sum('marks'))
    return marks['marks']
admin.site.register(Report, ReportDisplay)