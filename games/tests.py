from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Game

class GameTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_game = Game.objects.create(
            author = test_user,
            title = 'Mario',
            body = 'is depicted as a portly plumber who lives in the fictional land of the Mushroom Kingdom with Luigi, his younger, taller brother. In the television series and film, Mario and Luigi are originally from Brooklyn, New York.'
        )
        test_game.save() # Save the object to mock Database

    def test_blog_content(self):
        game = Game.objects.get(id=1)
        actual_author = str(game.author)
        actual_title = str(game.title)
        actual_body = str(game.body)
        self.assertEqual(actual_author, 'testuser')
        self.assertEqual(actual_title, 'Mario')
        self.assertEqual(actual_body, 'is depicted as a portly plumber who lives in the fictional land of the Mushroom Kingdom with Luigi, his younger, taller brother. In the television series and film, Mario and Luigi are originally from Brooklyn, New York.')