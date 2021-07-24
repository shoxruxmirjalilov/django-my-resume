from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) 
    summary = models.CharField(max_length=1000)
    text = models.TextField()

    def __str__(self):
        return self.title    
          