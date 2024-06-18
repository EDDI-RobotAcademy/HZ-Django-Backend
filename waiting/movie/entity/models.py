from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    movieName = models.CharField(max_length=128, null=False)
    movieReleaseDate = models.CharField(max_length=128, null=False)     # 개봉일자
    movieFilmRating = models.CharField(max_length=32, null=False)       # 영상물 등급
    movieGenre = models.CharField(max_length=128, null=False)
    movieCountry = models.CharField(max_length=128, null=False)         # 제작 국가
    movieRunningTime = models.CharField(max_length=32, null=False)
    movieSummary = models.TextField()
    moviePrice = models.DecimalField(max_digits=10, decimal_places=2)
    movieImage = models.CharField(max_length=100, null=True)

    # 추후 이미지 관련 필드 추가
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'movie'
