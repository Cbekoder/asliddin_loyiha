from django.db import models

class ScoreEntry(models.Model):
    idx = models.IntegerField()
    score = models.CharField(max_length=50)
    text = models.TextField(unique=True)

    def __str__(self):
        return f"{self.text[:50]}... ({self.score})"
