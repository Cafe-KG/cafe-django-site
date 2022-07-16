from rest_framework import serializers

from caterings.models import Catering, BookCatering


class CateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = ('title', 'description', 'address')


class BookCateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCatering
        fields = ('user', 'catering', 'date_book')
