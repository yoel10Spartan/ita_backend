from django.contrib import admin
from .models import Topic, SubTopic, Exercise, Answers, Equations

admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Exercise)
admin.site.register(Answers)
admin.site.register(Equations)