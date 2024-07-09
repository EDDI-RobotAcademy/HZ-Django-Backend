from rest_framework import serializers

from movie.entity.models import Movie


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movieId', 'movieName', 'movieReleaseDate', 'movieFilmRating', 'movieGenre', 'movieCountry',
                  'movieRunningTime', 'movieSummary', 'movieImage', 'movieRegisteredDate', 'movieUpdatedDate']

        read_only_fields = ['movieRegisteredDate', 'movieUpdatedDate']
        