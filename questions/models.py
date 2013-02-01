from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	info = models.CharField(max_length=300, blank=True)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
models.signals.post_save.connect(create_profile, sender=User)

class Question(models.Model):
	author = models.ForeignKey(Profile)
	title = models.CharField(max_length=140)
	question_text = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	author = models.ForeignKey(Profile)
	answer_text = models.TextField()
	votes = models.IntegerField()
	is_right = models.BooleanField()

	def __str__(self):
		return self.answer_text
