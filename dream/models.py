from django.db import models

NULLABLE = {'blank': True, 'null': True}


class DreamCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='dream category')
    description = models.TextField(verbose_name='dream category description', **NULLABLE)
    image = models.ImageField(upload_to='dream_image', verbose_name='dream category image', **NULLABLE)


class Dream(models.Model):
    title = models.CharField(max_length=200, verbose_name='dream')
    dream_category = models.ForeignKey(DreamCategory, on_delete=models.CASCADE, verbose_name='dream category')
    dream_image = models.ImageField(upload_to='dream_image', verbose_name='dream image', **NULLABLE)
    cost = models.IntegerField(verbose_name='dream cost', **NULLABLE)
    status = models.BooleanField(default=False, verbose_name='completion status')


