from django.db import models

# Create your models here.
class send_a_query(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    query = models.CharField(max_length=200)
    query_answered = models.BooleanField(default = False)
    
    
    class Meta:
        ordering = ["-id"]
        
    def __str__(self) -> str:
        return self.name + "'s query"
    
    
class newsletteremail(models.Model):
    email = models.EmailField()
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-id"]
        
    def __str__(self) -> str:
        email_status = 'inactive'
        if self.status:
            email_status = "active"
        return self.email + "| " + email_status
    
class project_details(models.Model):
    title = models.CharField(max_length=100) 
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["-id"]
        
    def __str__(self) -> str:
        return "Project: " + self.title
    