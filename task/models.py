from django.db import models
from .fields import EncryptedTextField
import uuid
# Create your models here.

class Task(models.Model):
    
    priority_choices = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = EncryptedTextField(max_length=200)
    description = EncryptedTextField(max_length=500)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=priority_choices)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-priority']