from django.db import models

# Category model
class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )

    title       = models.CharField(max_length = 30)
    keywords    = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    status      = models.CharField(max_length = 10, choices = STATUS)
    slug        = models.SlugField()
    parent      = models.ForeignKey('self', blank = True, null = True, related_name = 'children', on_delete = models.CASCADE)
    create_at   = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

# Product model
class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    
    category    = models.ForeignKey(Category, on_delete = models.CASCADE)
    title       = models.CharField(max_length = 30)
    keywords    = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    status      = models.CharField(max_length = 10, choices = STATUS)
    image       = models.ImageField(blank = True, upload_to = 'images')
    price       = models.FloatField()
    amount      = models.IntegerField()
    detail      = models.TextField()
    create_at   = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
    
    