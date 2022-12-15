from django.urls import path

from .views import (
    QuizView,
    QuizSelectedView,
    DisplayQuestionView,
    ResultView,
)

app_name = 'quiz'

urlpatterns = [
    path('', QuizView.as_view(), name='quiz'),
    path('quiz/<int:pk>/', QuizSelectedView.as_view(), name='quiz_select'),
    path('<int:quiz_id>/<int:question_id>/', DisplayQuestionView.as_view(), name='display_question'),
    path('result/', ResultView.as_view(), name='result'),
]
