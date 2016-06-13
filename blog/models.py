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

    def author(self):
        return self.author

    def title(self):
        return self.title

    def text(self):
        return self.text

    def published_date(self):
        return self.published_date

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Post(models.Model):
    def __init__(self, author, title, text, published_date):
        self.post_Data = PostData(author, title, text, published_date)

    def publish(self):
        return self.post_Data.publish

    def __str__(self):
        return self.post_Data.title

class CommentData(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def __init__(self, post, author, text, approved_comment):
        self.post = post
        self.author = author
        self.text = text
        self.approved_comment = approved_comment

    def post(self):
        return self.post

    def author(self):
        return self.author

    def text(self):
        return self.text

    def approved_comment(self):
        return self.approved_comment

class Comment(models.Model):
    def __init__(self, post, author, text, approved_comment):
        self.comment_data = CommentData(post, author, text, approved_comment)

    def approved_comment(self):
        return self.comment_data.pproved_comment

    def approve(self):
        self.comment_data.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_data.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
