from django.db import models

class Question(models.Model):
	question_text = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.TextField()
	votes = models.IntegerField()
	is_right = models.BooleanField()

	def __str__(self):
		return self.answer_text
