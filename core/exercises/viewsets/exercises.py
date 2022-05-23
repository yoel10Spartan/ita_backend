from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.exercises.serializers import ExercisesSerializer
from rest_framework.decorators import action
from core.exercises.db.exercises import Answers, Equations, Exercise

class ExercisesViewSet(viewsets.ModelViewSet):
    serializer_class = ExercisesSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Exercise.objects.all()
    
    def create(self, request, *args, **kwargs):
        equations = request.data['equations']
        equations_list = []
        
        for eq in equations:
            ob_eq = Equations.objects.create(**eq) 
            equations_list.append(ob_eq.pk)
          
        if request.data['type'] == 'ML':
            answers = request.data['answers']
            answers_list = []
                
            for ans in answers:
                ob_ans = Answers.objects.create(**ans) 
                answers_list.append(ob_ans.pk)
            
            
            request.data['answers'] = answers_list
            
        request.data['equations'] = equations_list
        
        return super().create(request, *args, **kwargs)