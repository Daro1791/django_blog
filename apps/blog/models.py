from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Category name', max_length=100, null=False, blank=False)
    state = models.BooleanField('Category enable/disabled', default=True)
    creation_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField('Author names', max_length=255, null=False, blank=False)
    surnames = models.CharField('Author surnames', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    mail = models.EmailField('E-Mail', null=False, blank=False)
    state = models.BooleanField('Author active/no active', default=True)
    creation_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return "{0}, {1}".format(self.surnames, self.names)    
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=100, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    description = models.CharField('Description', max_length=150, blank=False, null=False)
    content = RichTextField()
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    author = models.ForeignKey(Author,  on_delete=models.CASCADE)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    state = models.BooleanField('Published/Unpublished', default=True)
    creation_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title



