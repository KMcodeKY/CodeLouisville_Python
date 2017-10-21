from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class ToDo(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('checklist:detail', kwargs={'pk': self.pk})
