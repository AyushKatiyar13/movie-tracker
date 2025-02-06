from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

class WatchStatus(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
    date_watched = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'movie'], name='unique_watch_status')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.movie.name}"
