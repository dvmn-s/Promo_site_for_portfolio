from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250) #default='None
    full_text = models.TextField('Full_text')
    date = models.DateTimeField('Date of Publication')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
