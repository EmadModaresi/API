from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from API.models import models, Book
from API.serializers import BookModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


@permission_classes([IsAuthenticated])
class GetALLData(APIView):
    def get(self, request):
        query = Book.objects.all().order_by('-create_at')
        serializers = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


# Create your views here.
@permission_classes([IsAuthenticated])
class GetFavData(APIView):
    def get(self, request):
        query = Book.objects.filter(fav=True)
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class GetNotFavData(APIView):
    def get(self, request):
        query = Book.objects.filter(fav=False)
        serializer = BookModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAdminUser])
class UpgradeFavData(APIView):
    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookModelSerializer(query)
        return Response(serializers.data, status.HTTP_200_OK)

    def put(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookModelSerializer(query, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class PostModelData(APIView):
    def post(self, request):
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        query = Book.objects.all()
        serializer = BookModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAdminUser])
class SearchDdata(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Book.objects.filter(store_name__contains=search)
        serializer = BookModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAdminUser])
class DeleteData(APIView):
    def delete(self, request, pk):
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(status == status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def allApi(request):
    if request.method == 'GET':
        query = Book.objects.all().order_by('-create_at')
        serializer = BookModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAdminUser])
@api_view(['POST'])
def SetData(request):
    if request.method == "POST":
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        allApi(request)
