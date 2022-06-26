from django.db import IntegrityError
from django.test import TestCase

from post.models import Post, PostTag, Tag
from user.models import BaseUser


class TestPostModel(TestCase):
    def setUp(self) -> None:
        self.user = BaseUser.objects.create()
        self.post = Post.objects.create(
            title="Test post",
            text="Text of the post",
            author=self.user,
        )
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_create_empty_post_raises_exception(self):
        self.assertRaises(IntegrityError, Post.objects.create)

    def test_post_creation_is_ok(self):
        post = Post.objects.create(
            title="Test post",
            text="Text of the post",
            author=self.user,
        )

    def test_post_str_method(self):
        self.assertEquals(str(self.post), "Test post")

    def test_assign_tag_to_post(self):
        tag = Tag.objects.create(name="Django")
        self.post.tags.add(tag)
        self.assertTrue(self.post.tags.all())
        self.assertEquals(self.post.tags.first(), tag)

    def test_remove_tag_from_post(self):
        tag = Tag.objects.create(name="Django")
        self.post.tags.add(tag)
        self.post.tags.remove(tag)
        self.assertFalse(self.post.tags.all())
        self.assertEquals(self.post.tags.all().count(), 0)


class TestTagModel(TestCase):
    def test_empty_tag_raises_error(self):
        self.assertRaises(IntegrityError, Tag.objects.create)

    def test_tag_str_method(self):
        tag = Tag.objects.create(name="Tag number 1")
        self.assertEquals(str(tag), "Tag number 1")
