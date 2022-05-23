from rest_framework import serializers

from core.evaluation.db.evaluation import Evaluation
from core.user.serializers import UserSerializer

class EvaluationSerializer(serializers.ModelSerializer):
    # created_by = UserSerializer()
    
    class Meta:
        model = Evaluation
        fields = '__all__'