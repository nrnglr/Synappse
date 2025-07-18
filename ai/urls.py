from django.urls import path
from .views import (
    CreateCreativityExerciseView,
    ListCreativityExercisesView,
    CreativityTestPageView
)
from .views import (
    CreateMemoryExerciseView, 
    ListMemoryExercisesView
)

app_name = 'ai'

urlpatterns = [
    # Yaratıcılık egzersizlerini test etmek (oluşturmak ve listelemek) için kullanılan sayfa
    path('creativity/test/', CreativityTestPageView.as_view(), name='creativity-test-page'),

    # API endpoint: Yeni bir yaratıcılık egzersizi oluşturur (ve Supabase'e kaydeder)
    path('creativity/create/', CreateCreativityExerciseView.as_view(), name='create-creativity-exercise'),

    # API endpoint: Mevcut yaratıcılık egzersizlerini Supabase'den listeler
    path('creativity/exercises/', ListCreativityExercisesView.as_view(), name='list-creativity-exercises'),

    path('memory/create/', CreateMemoryExerciseView.as_view(), name='create-memory-exercise'),
    path('memory/exercises/', ListMemoryExercisesView.as_view(), name='list-memory-exercises'),
]
