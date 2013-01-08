from django.contrib import admin
from questions.models import Question, Answer

class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
