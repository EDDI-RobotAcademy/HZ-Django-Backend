from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    movieName = models.CharField(max_length=128, null=False)
    movieReleaseDate = models.DateField(null=False)
    movieFilmRating = models.CharField(max_length=32, null=False)
    movieGenre = models.CharField(max_length=128, null=False)
    movieCountry = models.CharField(max_length=128, null=False)
    movieRunningTime = models.CharField(max_length=32, null=False)
    movieSummary = models.TextField()
    movieImage = models.CharField(max_length=100, null=True)

    movieRegisteredDate = models.DateTimeField(auto_now_add=True)
    movieUpdatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'movie'
