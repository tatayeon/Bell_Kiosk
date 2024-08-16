from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, blank=True)

    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return f'/lgcon/category/{self.slug}/'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name, allow_unicode=True)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "categories"

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    menu_image = models.ImageField(upload_to='media/lgcon/menu_image/', blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"[{', '.join(category.category_name for category in self.categories.all())}] {self.name}"


class Order(models.Model):
    Order_at = models.DateTimeField(auto_now=True)

    order_name = models.CharField(max_length=30)

    price = models.IntegerField()

    quantity = models.IntegerField()

    bell_number = models.IntegerField()

