from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.exercises.serializers import SubTopicSerializer, TopicSerializer
from core.exercises.db.topic import Topic, SubTopic
from rest_framework.decorators import action

class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Topic.objects.all()
    
class SubTopicViewSet(viewsets.ModelViewSet):
    serializer_class = SubTopicSerializer
    permission_classes = (IsAuthenticated,)
    queryset = SubTopic.objects.all()
    
    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated])
    def get_for_topic(self, request, pk=None):
        sub_topics = self.queryset.filter(topic=pk)
        sub_topic_serializer = self.serializer_class(sub_topics, many=True)
        return Response(sub_topic_serializer.data)
    
    