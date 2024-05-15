from django.db import models

class People(models.Model):
    GENDER_CHOICES = (
        ('m', 'man'),
        ('w', 'woman'),
    )
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __str__(self):
        return self.name


class Children(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=People.GENDER_CHOICES)
    father = models.ForeignKey(People, related_name="father", on_delete=models.SET_NULL, null=True)
    monther = models.ForeignKey(People, related_name="mother", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class StoreIcecream(models.Model):
    adres = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=6, decimal_places=6)
    def __str__(self):
        return self.adres

class Ice(models.Model):
    TYPE_CHOICES = (
        ('пломбир', 'Пломбир'),
        ('лед', 'Лед'),
        ('эскимо', 'Эскимо'),
    )
    name = models.CharField(max_length=25, choices=TYPE_CHOICES)
    price = models.IntegerField(default=0)
    all_ice = models.ForeignKey(StoreIcecream, on_delete=models.CASCADE, related_name='ice')
    def __str__(self):
        return self.all_ice.name



