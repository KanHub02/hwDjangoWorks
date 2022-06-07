from django.test import TestCase
from . import models
from datetime import date


class TestModel(TestCase):
    def test_model_shows_create_success(self):
        payload = {
            'title': "Test title",
            'author': 'Test author',
            'description': 'Test description',
            'image': 'Test image',
            'genre': 'Test Genre',
            'quantity': 5,
            'created_date': date.today(),
            'updated_date': date.today(),
            'age_control': 18,

        }
        post = models.Book.objects.create(**payload)
        self.assertEqual(post.title, payload['title'])
        self.assertEqual(post.author, payload['author'])
        self.assertEqual(post.description, payload['description'])
        self.assertEqual(post.image, payload['image'])
        self.assertEqual(post.genre, payload['genre'])
        self.assertEqual(post.quantity, payload['quantity'])
        self.assertEqual(post.created_date, payload['created_date'])
        self.assertEqual(post.updated_date, payload['updated_date'])
        self.assertEqual(post.age_control, payload['age_control'])

    def test_model_shows_create_fail(self):
        payload = {
            'title': "Test title",
            'author': 'Test author',
            'description': 'Test description',
            'image': 'Test image',
            'genre': 'Test Genre',
            'quantity': 5,
            'created_date': date.today(),
            'updated_date': date.today(),
            'age_control': 'negr',

        }

        with self.assertRaises(ValueError):
            post = models.Book.objects.create(**payload)

        pass

    def test_model_shows_update(self):
        payload = {
            'title': "Test title",
            'author': 'Test author',
            'description': 'Test description',
            'image': 'Test image',
            'genre': 'Test Genre',
            'quantity': 5,
            'created_date': date.today(),
            'updated_date': date.today(),
            'age_control': 18,

        }
        newtitle = 'New Title'
        post = models.Book.objects.create(**payload)
        post.title = newtitle
        post.save()
        post.refresh_from_db()
        self.assertEqual(post.title, newtitle)

    def test_model_shows_delete(self):
        payload = {
            'title': "Test title",
            'author': 'Test author',
            'description': 'Test description',
            'image': 'Test image',
            'genre': 'Test Genre',
            'quantity': 5,
            'created_date': date.today(),
            'updated_date': date.today(),
            'age_control': 18,

        }
        post = models.Book.objects.create(**payload)
        pk = post.pk
        post.delete()
        with self.assertRaises(models.Book.DoesNotExist):
            models.Book.objects.get(pk=pk)
