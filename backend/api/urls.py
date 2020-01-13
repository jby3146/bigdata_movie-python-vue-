from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import login_views
from api.views import signup_views
from api.views import recommend_views
from api.views import question_views
from api.views import subscribe_views
from api.views import user_update_views
from api.views import searchuser
from api.views import insertrating
urlpatterns = [
    url('movies/$', movie_views.movies, name='movie_list'),
    url('users/$', auth_views.signup_many, name='user_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('login/$', login_views.login, name='login'),
    url('signup/$', signup_views.signup, name="signup"),
    url('recommends/$',recommend_views.recommend, name="recommend"),
    url('question/$',question_views.question, name="question"),
    url('subscribe/$',subscribe_views.subscribe, name="subscribe"),
    url('userupdates/$',user_update_views.user_update, name="user_update"),
    url('usermovieid/$',searchuser.user_search, name="user_search"),
    url('insertrating/$',insertrating.rating_insert, name="rating_insert"),
]
