from django.db import models


#Determines if a post is a WIP or published
STATUS = (
	(0, "Draft"),
	(1, "Publish")
)

#DB model for all blog posts
class Post(models.Model):
	title = models.CharField(max_length = 200, unique = True)
	slug = models.SlugField(max_length = 200, unique = True)
	updated_on = models.DateTimeField(auto_now = True)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add = True)
	post_status = models.IntegerField(choices = STATUS, default = 0)

	#Orders list of posts in DB by post recently created to oldest
	class Meta:
		ordering = ['-created_on']

	#Shows each post by it's title rather than it's PK
	def __str__(self):
		return self.title