from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    def __unicode__(self):
        return self.name
class Comment(models.Model):
    document = models.ForeignKey(Document,related_name="comments")
    text = models.TextField()
    