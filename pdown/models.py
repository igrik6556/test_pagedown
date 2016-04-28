from django.db import models


class Post(models.Model):
    text = models.TextField('Message')

    class Meta:
        db_table = 'Post'

    def __str__(self):
        return self.text[:10]
