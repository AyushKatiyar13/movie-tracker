from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    upcoming = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    def formatted_release_date(self):
        return self.release_date.strftime('%B %d, %Y')
