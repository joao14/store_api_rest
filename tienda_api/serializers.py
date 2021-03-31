from rest_framework import serializers
from tienda_api.models import *


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class ClientSerializer(serializers.Serializer):
    identification = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):

    tracks = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
