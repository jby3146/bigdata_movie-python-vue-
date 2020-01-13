from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie
from api.models import Rating
from api.models import Profile
from rest_framework.response import Response
from api.serializers import RatingUserSerializer, RatingMovieSerializer

@api_view(['GET','POST'])
def ratings(request):

    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('id', None))
        userid = request.GET.get('userid', None)
        ratings = Rating.objects.all()

        if id:
            ratings = ratings.filter(movieid=id)
            serializer = RatingUserSerializer(ratings, many=True)
        if userid:
            ratings = ratings.filter(userid=userid)

            for r in ratings :
                movie = Movie.objects.all().filter(id=r.movieid_id)
                mtitle = ''
                for m in movie :
                    mtitle = m.title
                r.movietitle = mtitle
            serializer = RatingMovieSerializer(ratings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        movieDb = Rating.objects.all()
        movieDb.delete()
        ratings = request.data.get('ratings', None)
        for rate in ratings:
            userid = rate.get('userid', None)
            profile = Profile.objects.get(id=userid)
            movieid = rate.get('movieid', None)
            rating = rate.get('rating', None)
            movie = Movie.objects.get(id=movieid)
            movie.ratings = float(movie.ratings)+float(rating)
            movie.viewCnt +=1
            movie.save()
            rating = rate.get('rating', None)
            Rating(userid=profile, movieid=movie, rating=rating, movietitle='').save()

        return Response(status=status.HTTP_200_OK)
