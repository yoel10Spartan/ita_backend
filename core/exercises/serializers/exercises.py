from rest_framework import serializers
from ..db.exercises import Equations, Exercise

class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        
        ret['equations'] = [ Equations.objects.get(pk=i).text for i in ret['equations'] ]
        ret['added_by'] = Exercise.objects.filter(added_by=ret['added_by']) \
                            .first() \
                            .added_by \
                            .get_full_name()
        
        return ret