# This file for manage DB How & Where save data
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

# For each Post we have: user - title - img - created

class Post(models.Model):
    # Now we created properties the Post in DB
    # The class as table in DB and the each property as column.
    user = models.ForeignKey(User, on_delete='None')
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    img = models.ImageField(upload_to='post_img/', default='post_img/20190116_185717.jpg')
    created = models.DateTimeField(default= timezone.now)

    def __str__(self):
        '''
        This method for return title of post
        If not write this method the name of post show
        Post object(1), Post object(2), ...
        :return: Post title
        '''
        return self.title
# If you created model you must add in setting file
# And you must makemigrations because django edit the DB
