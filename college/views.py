from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.http import HttpResponse

# Create your views here.
def get_students(request):
  queryset=Student.objects.all()

  # Q is a django operator used to perform search operations on multiple columns together 
  if request.GET.get('search'):
    queryset=Student.objects.filter(
      Q(student_id__studentId__icontains=request.GET.get('search'))|
      Q(name__startswith=request.GET.get('search'))|
      Q(department__department__startswith=request.GET.get('search'))|
      Q(email__icontains=request.GET.get('search'))|
      Q(address__startswith=request.GET.get('search'))
      )
    return render(request, 'students.html', {"page":"All Students", "page_obj":queryset})

  paginator = Paginator(queryset, 10)  # Show 10 contacts per page.
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request, 'students.html', {"page":"All Students", "page_obj":page_obj})


def see_marks(request, email)->None:
  allSubMarks=SubjectMarks.objects.filter(student__email=email)
  totalMarks=allSubMarks.aggregate(totalMarks=Sum('marks'))
  context={
    "page":"Marksheet",
    "allMarks":allSubMarks,
    "totalMarks":totalMarks,
  }
  return render(request, 'allMarks.html', context)