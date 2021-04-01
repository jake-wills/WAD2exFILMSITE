from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Film(models.Model):
    NAME_MAX_LENGTH = 128
    BIO_MAX_LENGTH = 500
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)

    rating = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    director = models.CharField(max_length=NAME_MAX_LENGTH)
    bio = models.CharField(max_length=BIO_MAX_LENGTH)
    img = models.ImageField(upload_to='film_images/', blank=True)
    category = models.PositiveSmallIntegerField(choices=(
        (1, "Action-Adventure"),
        (2, "Comedy"),
        (3, "Crime"),
        (4, "Horror"),
        (5, "Sci-fi"),
    ))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Film, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "films"

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __str__(self):
        return self.user.username




class Review(models.Model):
    REVIEW_MAX_LENGTH = 500
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)])
    reviewtext = models.CharField(max_length=REVIEW_MAX_LENGTH)
    def __str__(self):
        return self.rating



class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


