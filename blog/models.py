# Create your models here.

# Defining the Post model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)

    # title - field for the post title. CharField translates into VARCHAR column in SQL DB
    title = models.CharField(max_length=259)

    # Field intended to be used in URLs.  Usage for building SEO friendly URLs for blog posts
    # Django prevents multiple posts from having the same slug for a given date (attr. unique_for_date)
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # Author field defines a many-to-one relationship, meaning that each post is written by user and
    # user can write any number of posts. For this field Django will create a FK in db using PK of the
    # related model. Using CASCADE in attr. on_delete specifies the logic when user is deleted so all the
    # blogposts also will be deleted (SQL standard).
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    # Body of the post. Translates the dtype to TEXT feature in SQL.
    body = models.TextField()

    # This datetime indicating when the post was published.
    publish = models.DateTimeField(default=timezone.now)

    # This datetime indicates when the post was created.
    created = models.DateTimeField(auto_now_add=True)

    # This datetime indicates the last time the post was updated.
    updated = models.DateTimeField(auto_now=True)

    # Status shows status of a post defined above (draft, published).
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

