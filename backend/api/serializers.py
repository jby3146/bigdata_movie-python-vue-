from .models import Profile, Movie, Rating, Clustering , Question, Subscribe
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('username','gender','age','occupation')

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation', 'uidlist_array')

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff

class ClusteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clustering
        fields = ('id', 'gender', 'age', 'occupation', 'group')


class RatingUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('userid', 'rating')

class RatingMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('movieid', 'rating', 'movietitle')

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('name','title','content','replys','times')

class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'ratings', 'viewCnt', 'counting', 'mlist_array', 'imgpath', 'overview','production_companies_array','production_countries_array','runtime')

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('userid', 'period')
