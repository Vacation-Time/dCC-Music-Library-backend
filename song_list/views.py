from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongsSerializer
from .models import Songs


@api_view(['GET', 'POST'])
def songs_list(request):

    if request.method == 'GET':
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # checks incoming request against coded data
        serializer = SongsSerializer(data=request.data)
        # verifies of request is correct
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Updates SQL when request gets past above line when correct/True
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def song_detail(request, pk):
    song = get_object_or_404(Songs, pk=pk)
    if request.method == 'GET':
        serializer = SongsSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # checks incoming request against coded data
        serializer = SongsSerializer(song, data=request.data)
        # verifies of request is correct
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Updates SQL when request gets past above line when correct/True
        return Response(serializer.data)
