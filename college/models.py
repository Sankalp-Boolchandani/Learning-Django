from django.db import models

# Create your models here.

class Department(models.Model):
  department=models.CharField(max_length=100)

  def __str__(self)->str:
      return self.department
  
  class Meta:
     ordering = ["department"]

class StudentId(models.Model):
   studentId=models.CharField(max_length=100)

   def __str__(self):
       return self.studentId
   
class Student(models.Model):
   department=models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
   student_id=models.OneToOneField(StudentId, related_name="studentid", on_delete=models.CASCADE)
   name=models.CharField(max_length=100)
   age=models.IntegerField(default=18)
   email=models.EmailField(unique=True)
   address=models.TextField()

   def __str__(self):
       return self.name
   
   class Meta:
      ordering=['name']
      verbose_name='student'

class Subject(models.Model):
   subject_name=models.CharField(max_length=100)

   def __str__(self):
       return self.subject_name
   
class SubjectMarks(models.Model):
   student=models.ForeignKey(Student, related_name="student", on_delete=models.CASCADE)
   subject=models.ForeignKey(Subject, related_name="subject", on_delete=models.CASCADE)
   marks=models.IntegerField()

   def __str__(self):
       return f'{self.student} {self.subject}'   

   class Meta:
      unique_together=['student', 'subject']
      verbose_name_plural='Subject Marks'