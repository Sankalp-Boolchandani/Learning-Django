from faker import Faker
from .models import *
import random
from django.db.models import Sum

fake=Faker()

def create_students(n=10)->None:
  departments=Department.objects.all()
  for _ in range(n):
    #assigning department
    department_index=random.randint(0,3)
    department=departments[department_index]

    #creating studentid object for assigning to student
    student_id=str("STU-0"+str(random.randint(100,999)))
    student_id_object=StudentId()
    student_id_object.studentId=student_id
    student_id_object.save()
    
    #creating student object
    Student.objects.create(
      department=department,
      student_id=student_id_object,
      name=fake.name(),
      age=random.randint(18,25),
      email=fake.email(),
      address=fake.address()
    )

def create_student_marks()->None:
  students=Student.objects.all()
  for student in students:
    subjects=Subject.objects.all()
    for subject in subjects:
      SubjectMarks.objects.create(
        student=student,
        subject=subject,
        marks=random.randint(0,100)
      )
  generate_ranks()


def generate_ranks():
  ranks=Student.objects.annotate(total_marks=Sum('studentmarks__marks')).order_by('-total_marks', 'age')

  i=1
  for rank in ranks:
    Report.objects.create(
      student=rank,
      rank=i
    )
    i+=1