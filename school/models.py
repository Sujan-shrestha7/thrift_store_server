from django.db import models

class Teacher(models.Model):
    fullname = models.CharField(max_length=100, null=False, blank=False)
    email =  models.CharField(max_length=50, null=False, blank=False)
    password =  models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'teacher'
    
    def __str__(self):
        return f"fullname:{self.fullname}, email:{self.email}, password:{self.password}"

class Student(models.Model):
    fullname = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    student_class = models.CharField(max_length=20, null=False, blank=False)
    section = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        db_table = 'student'
    
    def __str__(self):
        return (f"fullname: {self.fullname},email: {self.email}, class: {self.student_class}, section: {self.section}")
