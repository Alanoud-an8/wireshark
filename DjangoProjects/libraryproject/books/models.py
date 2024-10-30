from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)         # حقل لعنوان الكتاب
    author = models.CharField(max_length=100)       # حقل لمؤلف الكتاب
    published_date = models.DateField()             # حقل لتاريخ النشر
    isbn = models.CharField(max_length=13, unique=True) # حقل لرقم ISBN ويجب أن يكون فريدًا

    def __str__(self):
        return self.title
