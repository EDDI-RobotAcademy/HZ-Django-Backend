from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from movie.entity.models import Movie
from movie.serializers import MovieSerializer
from movie.service.movie_service_impl import MovieServiceImpl

class MovieView(viewsets.ViewSet):
    queryset = Movie.objects.all()
    movieService = MovieServiceImpl.getInstance()

    def list(self, request):
        movieList = self.movieService.list()
        serializer = MovieSerializer(movieList, many=True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            movieName = data.get('movieName')
            movieReleaseDate = data.get('movieReleaseDate')
            movieFilmRating = data.get('movieFilmRating')
            movieGenre = data.get('movieGenre')
            movieCountry = data.get('movieCountry')
            movieRunningTime = data.get('movieRunningTime')
            movieSummary = data.get('movieSummary')
            movieImage = request.FILES.get('movieImage')


            if not all([movieName, movieReleaseDate, movieFilmRating, movieGenre, movieCountry,
               movieRunningTime, movieSummary, movieImage]):
                return Response({ 'error': '모든 내용을 채워주세요!' },
                                status=status.HTTP_400_BAD_REQUEST)

            self.movieService.createMovie(movieName, movieReleaseDate, movieFilmRating, movieGenre, movieCountry,
                                          movieRunningTime, movieSummary, movieImage)


            serializer = MovieSerializer(data=request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('영화 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readMovie(self, request, pk=None):
        movie = self.movieService.readMovie(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def removeMovie(self, request, pk=None):
        self.movieService.removeMovie(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyMovie(self, request, pk=None):
        movie = self.movieService.readMovie(pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)

        if serializer.is_valid():
            updatedMovie = self.movieService.updateMovie(pk, serializer.validated_data)
            return Response(MovieSerializer(updatedMovie).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

