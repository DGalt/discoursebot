from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return "{}: {}".format(self.title, self.text)
