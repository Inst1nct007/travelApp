from django.db import models


class Place(models.Model):
    CATEGORY_CHOICES = (
        ('IN', 'International'),
        ('DM', 'Domestic'),
    )
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=20, null=True)
    description = models.TextField()
    image = models.ImageField(default='landscape.jpg', upload_to='places')
    category = models.CharField(max_length=30, null=True, choices=CATEGORY_CHOICES)
    price = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class PlacesToVisit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='landscape.jpg', upload_to='places')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
