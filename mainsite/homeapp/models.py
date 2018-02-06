from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PDF(models.Model):
    uploader_name = models.TextField(blank=False)
    university = models.TextField(blank=False)
    pdfName = models.TextField(blank=False)
    professor_name = models.TextField(blank=False)
    subjectName = models.TextField(blank=False)
    pdf_title = models.TextField(blank=False)
    pdf_desc = models.TextField(blank=False)
    pdf_doc = models.FileField(upload_to='documents/')
    pdf_tags = ArrayField(
        models.CharField(max_length=15, blank=True),
        size=8,
        default=list,
        null=True)