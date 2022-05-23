from rest_framework.routers import SimpleRouter
from core.authentication.viewsets import (
    LoginViewSet, 
    RegistrationViewSet, 
    RefreshViewSet,
    RefreshDataViewSet
)
from .exercises.viewsets import ExercisesViewSet, TopicViewSet, SubTopicViewSet
from .evaluation.viewsets import EvaluationViewSet

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'auth/refresh_data', RefreshDataViewSet, basename='auth-refresh-data')

# EXERCISES
routes.register(r'exercises', ExercisesViewSet, basename='exercises')

# TOPICS
routes.register(r'topic', TopicViewSet, basename='topics')
routes.register(r'subtopic', SubTopicViewSet, basename='subtopics')

# EVALUATION
routes.register(r'evaluation', EvaluationViewSet, basename='evaluation')

urlpatterns = [
    *routes.urls,
]