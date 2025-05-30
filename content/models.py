from django.db import models

# Create your models here.
class War(models.Model):
    name = models.CharField(max_length=100)
    start = models.IntegerField()
    end = models.IntegerField()
    contextWar = models.TextField(default="")
    imageWar = models.URLField(default=0)
    belligerents = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Era(models.Model):
    name = models.CharField(max_length=100)
    start = models.IntegerField()
    end = models.IntegerField()
    contextEra = models.TextField()
    imageEra = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    war = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    casualties = models.IntegerField(default=0)
    image = models.URLField(max_length=300)
    imageWar = models.URLField(max_length=300)
    tactics_link = models.CharField(max_length=200)
    tactics = models.TextField()
    imageTactics = models.URLField(max_length=300)
    context = models.ForeignKey(War, on_delete=models.CASCADE, related_name='articles')
    eras = models.ManyToManyField(Era, related_name='articles')
    order = models.IntegerField(default=0)


    def __str__(self):
        return self.title[:20]