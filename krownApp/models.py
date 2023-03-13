from django.db import models
from pytils.translit import slugify

class Genre(models.Model):
    genreName = models.CharField("Genre", max_length=255)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.genreName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genreName)
        super().save(*args, **kwargs)

class Movie(models.Model):
    movieName = models.CharField("Movie name", max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")
    year = models.IntegerField("Year")
    producer = models.CharField("Producer", max_length=255)
    cover = models.CharField("Link to cover", max_length=500)
    poster = models.CharField("Link to poster", max_length=500)
    isTop = models.BooleanField("Is Top", default=False)
    isRecommended = models.BooleanField("Is Recommended", default=False)
    description = models.TextField("Description")
    rating = models.FloatField("Rating")
    movieLink = models.CharField("Link to movie", max_length=500)

    def __str__(self):
        return f"{self.movieName}"
