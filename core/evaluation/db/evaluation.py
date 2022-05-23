from django.db import models

from core.exercises.db.exercises import Exercise
from core.user.models import User

class Evaluation(models.Model):
    topic = models.CharField(max_length=100)
    subtopic = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, blank=True)
    # students = ''  # Agregar una vez que se tenga el modelo de estudiantes
    
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return '{} - Created By {}'.format(self.subtopic, self.created_by.name)