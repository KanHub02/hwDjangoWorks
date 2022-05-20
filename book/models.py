from django.db import models


# Create your models here.
class Book(models.Model):
    GENRE_CHOICE = (
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Comedy", "Comedy"),
        ("Education", "Education"),
        ("Sci-Fi", "Sci-Fi"),
        ("Manga", "Manga"),
        ("Romantic", "Romantic"),
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
    quantity = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    age_control = models.PositiveIntegerField()

    def __str__(self):
        return self.title
