from django.db import models

class Author(models.Model):
    photo = models.ImageField(upload_to="")
    name = models.CharField(max_length=50)
    date_birth = models.IntegerField()
    story = models.CharField(max_length=350)
    favorite_genre = GENRE_CHOICE = (
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Comedy", "Comedy"),
        ("Education", "Education"),
        ("Sci-Fi", "Sci-Fi"),
        ("Manga", "Manga"),
        ("Romantic", "Romantic"),
    )
    def __str__(self):
        return self.name