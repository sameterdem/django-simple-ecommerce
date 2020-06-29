from django.db import models

# Product category model
class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )

    title       = models.CharField(max_length = 100)
    keywords    = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    status      = models.CharField(max_length = 10, choices = STATUS)
    slug        = models.SlugField(max_length = 200, default = "")
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
    title       = models.CharField(max_length = 150)
    keywords    = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    status      = models.CharField(max_length = 10, choices = STATUS)
    slug        = models.SlugField(max_length = 200, default = "")
    image       = models.ImageField(blank = True, upload_to = 'images')
    price       = models.FloatField()
    amount      = models.IntegerField()
    detail      = models.TextField()
    create_at   = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

# Product image model
class Images(models.Model):
    products    = models.ForeignKey(Product, on_delete = models.CASCADE)
    title       = models.CharField(max_length = 50, blank = True)
    image       = models.ImageField(blank = True, upload_to = 'images/')

    def __str__(self):
        return self.title
    




    
    
    