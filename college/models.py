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
   

# Model manager class. Used for performing operations like soft delete. ex: in an enterprise software you dont delete all the data 
# from DB. You perform soft delete which is data is there in the DB but is not shown to users
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
   

class Student(models.Model):
   department=models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
   student_id=models.OneToOneField(StudentId, related_name="studentid", on_delete=models.CASCADE)
   name=models.CharField(max_length=100)
   age=models.IntegerField(default=18)
   email=models.EmailField(unique=True)
   address=models.TextField()
   is_deleted=models.BooleanField(default=False)

   objects=StudentManager()            # Student.objects.all() will give data with is_deleted field as false
   admin_objects=models.Manager()            # Student.admin_objects.all() will give data with is_deleted field as True i.e complete data

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
   student=models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
   subject=models.ForeignKey(Subject, related_name="subject", on_delete=models.CASCADE)
   marks=models.IntegerField()

   def __str__(self):
       return f'{self.student} {self.subject}'   

   class Meta:
      unique_together=['student', 'subject']
      verbose_name_plural='Subject Marks'


class Report(models.Model):
   student=models.ForeignKey(Student, related_name="studentrank", on_delete=models.CASCADE)
   rank=models.IntegerField()
   date_of_rank_generation=models.DateField(auto_now_add=True)

   class Meta:
      unique_together = ['student', 'date_of_rank_generation']