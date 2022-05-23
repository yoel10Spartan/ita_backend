from django.db import models
from django.utils.translation import gettext_lazy as _
from .topic import SubTopic, Topic
from core.user.models import User

class Equations(models.Model):
    text = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return 'Equation - {}'.format(self.id)
    
class Answers(models.Model):
    text = models.CharField(max_length=255)
    is_correct_answer = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return 'Answer - {}'.format(self.id)

class Exercise(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=500)
    
    equations = models.ManyToManyField(Equations)
    answers = models.ManyToManyField(Answers, blank=True)
    
    class TypeAnswer(models.TextChoices):
        MULTIPLE = 'ML', _('MULTIPLE')
        OPEN = 'OP', _('OPEN')
    
    type = models.CharField(
        max_length=2,
        choices=TypeAnswer.choices,
        default=TypeAnswer.OPEN
    )
    
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return 'Exercise {} added by {}'.format(self.pk, self.added_by.name)