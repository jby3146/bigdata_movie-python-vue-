from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)
    uidlist = models.CharField(max_length=200)
    @property
    def uidlist_array(self):
        return self.uidlist.strip().split('|')

#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    ratings = models.FloatField(default=10)
    viewCnt = models.IntegerField(default=10)
    counting = models.IntegerField(default=0)
    mlist = models.CharField(max_length=200)
    imgpath = models.CharField(max_length=200)
    overview = models.TextField()
    production_companies = models.CharField(max_length=200)
    production_countries = models.CharField(max_length=200)
    runtime = models.IntegerField()

    def __str__(self):
        return self.title
    @property
    def genres_array(self):
        return self.genres.strip().split('|')
    @property
    def mlist_array(self):
        return self.mlist.strip().split('|')
    @property
    def production_companies_array(self):
        return self.production_companies.strip().split('|')
    @property
    def production_countries_array(self):
        return self.production_countries.strip().split('|')

class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    movietitle = models.CharField(max_length=200)

class Clustering(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)
    group = models.IntegerField(default=0)

class Question(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    replys = models.TextField(blank=True)
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.title

    def __str__(self):
        return self.content

class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    userID = models.CharField(max_length=300)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.choice_text

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    userid = models.IntegerField(primary_key=True)
    period = models.CharField(max_length=100)
