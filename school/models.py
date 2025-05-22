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


class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='assignments/', null=True, blank=True)
    homework = models.TextField(blank=True)
    assigned_class = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title