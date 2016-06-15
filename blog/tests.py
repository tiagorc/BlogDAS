from django.test import TestCase
from .models import Post, Comment
from model_mommy import mommy
# from model_mommy.recipe import Recipe, foreign_key


# Create your tests here.
class PostFactory:
    def make_post(self):
        post = mommy.make(Post)
        return post

    def make_post_blank_text(self):
        return Post.objects.create(text="")

    def make_comment(self):
        comment = mommy.make(Comment)
        return comment


class PostTestCase(TestCase):
    def setUp(self):
        self.blank_message = PostFactory().make_post()

    def test_make_post(self):
        # pass
        post = PostFactory().make_post()
        self.assertEqual(post.__str__(), post.title)

    def test_make_comment(self):
        comment = PostFactory().make_comment()
        self.assertEqual(comment.__str__(), comment.text)
