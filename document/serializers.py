from rest_framework import serializers
from document.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class DocumentVerifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('verification_status',)
