from django.db import models

# model named Post
class CommentModel(models.Model):
	name = models.CharField( max_length = 100, blank = False,null = False)
	comment = models.TextField(blank = False, null = False)
	time = models.DateTimeField(auto_now_add = True)
