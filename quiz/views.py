from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .score import Score

from django.urls import reverse
from .models import (
    Quiz,
    Question,
    Answer,
    User,
    Marks_Of_User,
)


class QuizView(TemplateView):

    template_name = "quiz/quiz.html"
    def get(self, request):
        if request.user.is_anonymous:
            return redirect('account:login')
        quizs = Quiz.objects.all()
        context = {
            'quizs': quizs,
        }
        return render(request, self.template_name, context)


class QuizSelectedView(TemplateView):
    template_name = "quiz/quiz_selected.html"

    def get(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)
        question = quiz.question_set.first()
        return redirect(reverse('quiz:display_question', kwargs={"quiz_id": pk, "question_id": question.pk}))


class DisplayQuestionView(TemplateView):
    template_name = "quiz/display_question.html"

    def get(self, request, quiz_id, question_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = quiz.question_set.all()
        score = Score.get_ScoreforOneAnswer(quiz)
        request.session['puan'] = score
        request.session['score'] = 0
        request.session['quiz_id'] = quiz.id

        answers = []
        current_question, next_question = None, None

        for ind, question, in enumerate(questions):
            if question.pk == question_id:
                answers_q = Answer.objects.filter(question=question)
                correct_answer = Answer.objects.filter(question=questions[ind]).filter(correct=True).values('content')
                for a in answers_q:
                    answers.append(a)
                current_question = question
                if ind != len(questions)-1:
                    next_question = questions[ind + 1]

        return render(self.request,
                      self.template_name,
                      {"quiz": quiz,
                       "question": current_question,
                       "next_question": next_question,
                       "answers": answers,
                       "correct_answer": correct_answer})

    def post(self, request, quiz_id, question_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = quiz.question_set.all()
        b = request.POST
        answers = []
        count_puan = 0
        current_question, next_question = None, None
        corrct_answer, answer = [], []
        for ind, question, in enumerate(questions):
            if question.pk == question_id:
                answers_q = Answer.objects.filter(question=question)
                for a in answers_q:
                    answers.append(a)
                current_question = question
                corrct_answer = Answer.objects.filter(question=questions[ind-1]).filter(correct=True).values('content')
                answer = Answer.objects.filter(question=questions[ind-1]).filter().values('content')
                for i in answer:
                    try:
                        if (str(i['content']) == str(b[i['content']]) and i in corrct_answer):
                            count_puan += 1
                        print(str(i['content']) == str(b[i['content']]) and i in corrct_answer)
                    except:
                        print("ERROR")
                if ind != len(questions) - 1:
                    next_question = questions[ind + 1]
            if count_puan != 0:
                request.session['score'] += count_puan * request.session['puan']
                count_puan = 0
        if next_question is None:
            request.session['last_question'] = questions.last().id
        return render(self.request,
                          self.template_name,
                          {"quiz": quiz,
                           "question": current_question,
                           "next_question": next_question,
                           "answers": answers,
                           "correct_answer": corrct_answer})


class ResultView(TemplateView):
    template_name = 'quiz/result.html'

    def post(self, request):
        quiz = Quiz.objects.get(pk=request.session['quiz_id'])
        last_question_id = request.session['last_question']
        answer = Answer.objects.filter(question_id=last_question_id).\
                                    filter(correct=True).values('content')
        count_score = 0
        b = request.POST
        try:
            for item in answer:
                print(str(item['content']) == str(b[item['content']]))
                if (item['content'] in b[item['content']]):
                    count_score += 1
            request.session['score'] += count_score * request.session['puan']
        except:
            pass
        try:
            score = request.session['score']
            del request.session['score']
            del request.session['puan']
            del request.session['last_question']
            request.session.save()
        except:
            score = 0
        user_mark(request.user, quiz, score)
        return render(request, self.template_name, {'score': score})


def user_mark(user, quiz, score=0):
    return Marks_Of_User.objects.create(user = user, quiz=quiz, score=score)

