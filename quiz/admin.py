from django.contrib import admin
from nested_admin.nested import NestedModelAdmin, NestedStackedInline
from django import forms
from django.core.exceptions import ValidationError
from .models import (
    Quiz,
    Question,
    Answer,
    Marks_Of_User,
)

class AnswerForm(forms.ModelForm):
    correct = []
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionInline(NestedStackedInline):
    model = Question
    extra = 1

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    form = AnswerForm


class QuestionAdmin(admin.ModelAdmin):
    change_form_template = "quiz/change_list.html"
    save_on_top = True
    inlines = [AnswerInline]


class QuizAdmin(NestedModelAdmin):

    save_on_top = True
    inlines = [
        QuestionInline,
    ]


admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Marks_Of_User)