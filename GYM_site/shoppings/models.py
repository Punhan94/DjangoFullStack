from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.base import Model
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone

# Create your models here.

class Category(MPTTModel):
    Status = (
        ('True', 'Hə'),
        ('False','Yox'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to ='images/')
    status = models.CharField(max_length=10, choices=Status)
    slug = models.SlugField()
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by =['title']

    def __str__(self):
        full_path = [self.title]
        ka = self.parent
        while ka is not None:
            full_path.append(ka.title)
            ka = ka.parent
        return '>'.join(full_path[::-1])

    


class Product(models.Model):
    STATUS = (
        ('True', 'Hə'),
        ('False','Yox'),
    )
    category = models.ManyToManyField(Category)
    sold = models.PositiveIntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0, editable=False)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to ='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextField()
    slug = models.SlugField(blank=True, max_length=150)
    status = models.CharField(max_length=10, choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50px" />'.format(self.image.url))
    image_tag.short_description = 'Image'
    
    # def save(self, *args, **kvargs):
    #     return super(Product, self).save(*args, **kvargs)


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.title
    
class ShoppingComment(models.Model):
    STATUS = (
        ('New','Yeni'),
        ('True','Hə'),
        ('False','Yox'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=100 ,verbose_name='Adınızı qeyd edin')
    comment_email = models.EmailField(verbose_name='Emailinizi yazin')
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=400, blank=True)
    rate = models.IntegerField(default=1,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
            ]
    )
    status = models.CharField(max_length=20, choices=STATUS, default="New" )
    ip = models.CharField(blank=True, max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.subject