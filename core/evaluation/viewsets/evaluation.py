from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from core.evaluation.db.evaluation import Evaluation
from core.evaluation.serializers.evaluation import EvaluationSerializer

class EvaluationViewSet(ModelViewSet):
    serializer_class = EvaluationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Evaluation.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)

        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            self.get_queryset().filter(created_by=request.user)
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=True, permission_classes=[IsAuthenticated])
    def update_evaluation(self, request, pk=None):
        evaluation = Evaluation.objects.filter(pk=pk).first()
        
        for i in request.data['exercises']:
            evaluation.exercises.add(i)
            
        return Response({'ok': True})