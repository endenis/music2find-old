from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from questions.models import Profile, Question, Answer

class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
