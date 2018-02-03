from django.db import models
from django.contrib.postgres.fields import ArrayField


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PDF(models.Model):
    pdfName = models.CharField(max_length=255, blank=False)
    subjectName = models.CharField(max_length=50, blank=False)
    pdf_title = models.CharField(max_length=50, blank=False)
    pdf_desc = models.ForeignKey('description.Document', on_delete=models.CASCADE)
    pdf_doc = models.FileField(upload_to='documents/')
    pdf_tags = ArrayField(ArrayField(models.CharField(max_length=15, blank=True), size=8), size=8) #JSON to String
