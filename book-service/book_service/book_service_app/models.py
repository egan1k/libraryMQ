from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name

