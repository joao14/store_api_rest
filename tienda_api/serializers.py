from rest_framework import serializers

class HelloSerializer(serializers.Serializer):

    name= serializers.CharField(max_length=10)


class ClientSerializer(serializers.Serializer):

    identification = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)

class StoreSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)
    direction = serializers.CharField(max_length=100)

class ProductSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    stock = serializers.IntegerField(default=0)