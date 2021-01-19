from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField("person's first name", max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=None, blank=True)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, blank=True)


class Musician(Person):
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
