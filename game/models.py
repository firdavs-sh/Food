from django.db import models
from django.contrib.auth.models import User
from game.snippets import generate_unique_slug, choices
from django.utils.text import slugify

class Restaurant1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='restaurants/')
    categories1 = models.CharField(max_length=120)
 
   
    file=models.FileField(upload_to="restaurants/")
    details = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    views = models.IntegerField(default=0,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

    def get_categories(self):
        cats = self.categories1.split(',')
        return cats

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Restaurant1, self.title)
        else:  # create
            self.slug = generate_unique_slug(Restaurant1, self.title)
        super().save(*args, **kwargs)

    def delete(self,*args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class Reklama(models.Model):
    field=models.FileField(upload_to='restaurants/')
    malumot=models.CharField(max_length=200)
    def __str__(self) :
        return self.malumot

class Comment1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Restaurant1, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[::-1]