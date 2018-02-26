from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Document(models.Model):
    description = models.TextField(blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PDF(models.Model):
    uploaders = models.TextField(blank=True)
    university = models.TextField(blank=True)
    pdfName = models.TextField(blank=True)
    professor_name = models.TextField(blank=True)
    subjectName = models.TextField(blank=True)
    # pdf_title = models.TextField(blank=True)
    pdf_desc = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #pdf_doc = models.FileField(upload_to='documents/')
    pdf_tags = ArrayField(
        models.CharField(max_length=150, blank=True),
        size=8,
        default=list,
        null=True)

class Tag(models.Model):
    tagName=models.TextField(blank=False,unique=True)
    count=models.IntegerField(blank=False)