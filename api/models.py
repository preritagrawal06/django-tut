from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos") # related_name creates a field in user model named "todos" which can help in querying all the todos created by a specific user rather than searching in todos for a specific user
    
    def __str__(self):
        return self.title
    
