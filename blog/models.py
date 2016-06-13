from django.db import models
from django.utils import timezone


class TimestampedMixin(models.Model):
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class PostData(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __init__(self, author, title, text, published_date):
        self.author = author
        self.title = title
        self.text = text
        self.published_date = published_date

    @property
    def author(self):
        return self.author
    @property
    def title(self):
        return self.title
    @property
    def text(self):
        return self.text
    @property
    def published_date(self):
        return self.published_date

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Post(models.Model):
    def __init__(self, author, title, text, published_date):
        self.post_Data = PostData(author, title, text, published_date)

    def author(self):
        return self.post_Data.author

    def title(self):
        return self.post_Data.title

    def text(self):
        return self.post_Data.text

    def published_date(self):
        return self.post_Data.published_date

    def publish(self):
        return self.post_Data.publish

    def __str__(self):
        return self.post_Data.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
