from django.conf import settings
from .models import Question

class Score(object):
    def __init__(self, request):
        self.session = request.session
        score = self.session.get(settings.SCORE_SESSION_ID)
        if not score:
            score = self.session[settings.SCORE_SESSION_ID] = {}
        self.score = score

    def add(self, quiz, puan = 0):
        if puan == 0:
            self.score[quiz.name] = 0
        else:
            puan = float(self.score[quiz.name]) + puan
            self.score[quiz.name] = puan

    @staticmethod
    def get_ScoreforOneAnswer(quiz):
        return 100 / len(Question.objects.filter(quiz=quiz).filter(answer__correct=True))


    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.SCORE_SESSION_ID]
        self.session.modified = True

    def save(self):
        # Обновление сессии cart
        self.session[settings.SCORE_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True
