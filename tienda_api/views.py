from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tienda_api import serializers
from tienda_api.models import *
import json


class HelloAppiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retorna un objeto """
        data = [
            'Alex',
            'Martina',
            'Martina'
        ]
        return Response({'message': 'Hello', 'data': data})

    def post(self, request):
        """ Crear un objeto"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Actualización de un objeto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Actualización parcial de un registro"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Eliminar un registro"""
        return Response({'method': 'DELETE'})


class ClientAppiView(APIView):
    serializer_class = serializers.ClientSerializer

    def post(self, request):
        """Create new client in this app"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Client.objects.create(
                identification=serializer.validated_data.get('identification'),
                name=serializer.validated_data.get('name'),
                lastname=serializer.validated_data.get('lastname'),
                email=serializer.validated_data.get('email'),
                phone=serializer.validated_data.get('phone'))
            client = Client.objects.all().filter(
                identification=serializer.validated_data.get('identification')).values()
            message = 'Client created success'
        else:
            message = 'CLient haven´t been created'

        return Response({'message': message, 'data': client})


class StoreAppiView(APIView):
    serializer_class = serializers.StoreSerializer

    def get(self, request):
        store = Store.objects.all().values()
        return Response({'message': 'Consult success', 'store': store})

    def post(self, request):
        """Create new store with all your informations"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Store.objects.create(
                name=serializer.validated_data.get('name'),
                phone=serializer.validated_data.get('phone'),
                direction=serializer.validated_data.get('direction')
            )
            message = "Store created"
            store = Store.objects.all().values()
        else:
            message = "Store invalid"

        return Response({'message': message, 'stores': store})


class ProductAppiView(APIView):
    serializer_class = serializers.ProductSerializer

    def get(self, request):
        product = Product.objects.all().values()
        return Response({'message': 'Consult success', 'product': product})

    def post(self, request):
        """Create new product to each store"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Product.objects.create(
                name=serializer.validated_data.get('name'),
                stock=serializer.validated_data.get('stock'),
                store_id=serializer.validated_data.get('store_id')
            )
            products = Product.objects.all().values()
            message = "Product created"
        else:
            message = "Product invalid"

        return Response({'message': message, 'products': products})


class AlbumApiView(APIView):
    serializer_class = serializers.AlbumSerializer

    def get(self, request):
        albums = Album.objects.all().values()
        return Response({'albums': albums})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Album.objects.create(
                album_name=serializer.validated_data.get('album_name'),
                artist=serializer.validated_data.get('artist')
            )
            album = Album.objects.filter(album_name=serializer.validated_data.get('album_name')).values()
            message = 'Album created'
        else:
            message = 'Album has been a error'
        return Response({'message': message, 'album': album})


class TrackApiView(APIView):
    serializer_class = serializers.TrackSerializer

    def get(self, request):
        albums = Track.objects.all().values()
        return Response({'tracks': albums})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Track.objects.create(
                order=serializer.validated_data.get('order'),
                title=serializer.validated_data.get('title'),
                duration=serializer.validated_data.get('duration'),
                album=serializer.validated_data.get('album')
            )
            track = Track.objects.filter(album=serializer.validated_data.get('album')).values()
            message = 'Track created'
        else:
            message = 'Track has been a error'
        return Response({'message': message, 'album': track})
