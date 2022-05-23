from rest_framework import serializers
from ..db.topic import Topic, SubTopic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        
class SubTopicSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    
    class Meta:
        model = SubTopic
        fields = '__all__'