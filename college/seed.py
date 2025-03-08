from faker import Faker
from .models import *
import random

fake=Faker()

def create_stu_id_obj():
  id=str(random.randint(100,999))
  StudentId.objects.create(studentId="STU-0"+id)
  return StudentId.objects.get(studentId="STU-0"+id)

def create_students(n=10)->None:
  departments=Department.objects.all()
  for _ in range(n):
    department_index=random.randint(0,3)
    department=departments[department_index]

    student_id=create_stu_id_obj()

    Student.objects.create(
      department=department,
      student_id=student_id,
      name=fake.name(),
      age=random.randint(18,25),
      email=fake.email(),
      address=fake.address()
    )