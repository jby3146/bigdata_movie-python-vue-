from django.contrib.auth.models import User
from api.models import Profile
from .models import Movie,Profile,Rating
from .models import Post
from .models import Question,Reply
from django.contrib import admin


admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(Rating)

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name','title','content')
    fieldsets = [
        ('Name',          {'fields':['name']}),
        ('Time',          {'fields':['times']}),
        ('Title',            {'fields':['title']  }),
        ('Content',          {'fields':['content']}),
        ('Reply',          {'fields':['replys']})
    ]
    inlines = [ReplyInline]

admin.site.register(Question, QuestionAdmin)


class PostWriting(admin.ModelAdmin):
    list_display = ('title','created_date', 'author','content')

admin.site.register(Post, PostWriting)
