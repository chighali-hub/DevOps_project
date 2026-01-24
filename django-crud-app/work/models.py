from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name=models.CharField(max_length=255)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    charge=models.IntegerField()
    description=models.TextField()
    
    def __str__(self):
        return self.name 

class Modules(models.Model):
    name=models.CharField(max_length=255)
    Category=models.ForeignKey(Courses,on_delete=models.CASCADE)
    description=models.TextField()
    
    def __str__(self):
        return self.name 


    
class Members(models.Model):
    GEN= (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
    )
    name=models.CharField(max_length=255)
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=20, choices=GEN, default='M')    
    photo=models.ImageField(upload_to='photo/')    
    def __str__(self):
        return self.name 
    
class Blogs(models.Model):
    title=models.CharField(max_length=255)
    Category=models.ForeignKey(Courses,on_delete=models.CASCADE)  
    description=models.TextField()
    photo=models.ImageField(upload_to='photo')    
    uploadedBy=models.ForeignKey(Members,on_delete=models.CASCADE)
    def __str__(self):
        return self.title 