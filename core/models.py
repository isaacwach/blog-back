from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def _str_ (self):
        return self.title
