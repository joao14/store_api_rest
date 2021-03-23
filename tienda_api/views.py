from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tienda_api import serializers


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
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Actualización parcial de un registro de la base de datos"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Eliminar un registro"""
        return Response({'method': 'DELETE'})