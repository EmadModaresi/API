from rest_framework import serializers
from datetime import datetime
from API.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
