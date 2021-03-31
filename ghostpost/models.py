from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    ROAST = 'Roast'
    BOAST = 'Boast'
    CHOICES = [
        (ROAST, 'Roast'),
        (BOAST, 'Boast'),
    ]
    post_type = models.CharField(max_length=7, choices=CHOICES)
    post = models.CharField(max_length=280)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    # total_votes = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.post} | {self.post_type} "
    
    @property
    def score(self):
        return self.upvote - self.downvote
    
