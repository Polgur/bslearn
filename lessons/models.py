from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name.title()

class Book(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    author = models.CharField(max_length=40, blank=True )
    year = models.SmallIntegerField(blank=True)
    link = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Книга (Видеокурс)'
        verbose_name_plural = 'Книги (Видеокурсы)'

    def __str__(self):
        return self.name.title()

class Lesson(models.Model):
    prn = models.ForeignKey(Book, related_name='lessons')
    part = models.SmallIntegerField()
    numb = models.SmallIntegerField()
    name = models.CharField(max_length=40, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    desc = models.TextField()
    template = models.CharField(max_length=80)

    class Meta:
        ordering = ('part', 'numb',)
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


    def __str__(self):
        return self.name.title()