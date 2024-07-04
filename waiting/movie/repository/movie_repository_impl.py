import os

from waiting import settings
from movie.entity.models import Movie
from movie.repository.movie_repository import MovieRepository


class MovieRepositoryImpl(MovieRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Movie.objects.all().order_by('movieRegisteredDate')

    def create(self, movieName, movieReleaseDate, movieFilmRating, movieGenre,
               movieCountry, movieRunningTime, movieSummary, movieImage):
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            'C:/TeamProject/SK-Networks-AI-1/HZ/HZ-Vue-Frontend/src/assets/images/uploadImages'
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, movieImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in movieImage.chunks():
                destination.write(chunk)

            destination.flush()
            os.fsync(destination.fileno())

        movie = Movie(
            movieName=movieName,
            movieReleaseDate=movieReleaseDate,
            movieFilmRating=movieFilmRating,
            movieGenre=movieGenre,
            movieCountry=movieCountry,
            movieRunningTime=movieRunningTime,
            movieSummary=movieSummary,
            movieImage=movieImage.name,

        )
        movie.save()
        return movie

    def findByMovieId(self, movieId):
        try:
            return Movie.objects.get(movieId=movieId)
        except Movie.DoesNotExist:
            return None

    def deleteByMovieId(self, movieId):
        movie = Movie.objects.get(movieId=movieId)
        movie.delete()

    def update(self, movie, movieData):
        for key, value in movieData.items():
            print(f"key: {key}, value: {value}")
            # 쉽게 생각해보자면 movie 라는 Entity가 가지고 있는 속성값 중
            # 현재 수정 요청에 의해 전달된 정보에 대응되는 key가 가지고 있는 value 값을 갱신시킴
            setattr(movie, key, value)

        movie.save()
        return movie
