from rest_framework import serializers

from homeapp.models import PDF
from signupapp.models import UserTable


class SearchSerializers(serializers.ModelSerializer):
    pdf_tags = serializers.ListField(child=serializers.CharField(max_length=15, allow_blank=True))

    class Meta:
        model = PDF
        fields = ('uploaders', 'pdfName', 'professor_name', 'subjectName', 'pdf_desc', 'pdf_tags', 'university', 'id')