from rest_framework import viewsets, filters
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
