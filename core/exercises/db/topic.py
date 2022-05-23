from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class SubTopic(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return '{} - {}'.format(self.name, self.topic.name)