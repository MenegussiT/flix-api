import json
from django.http import JsonResponse
from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializers import GenreSerializer

class GenereCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = []
#         for genre in genres:
#             data.append({
#                 'id': genre.id,
#                 'name': genre.name
#             })
#         return JsonResponse(data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201,)
    
@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method=='GET':
        data = { 'id': genre.id, 'name': genre.name }
        return JsonResponse(data)
    
    elif request.method=='PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name}, status=200,)

    elif request.method=='DELETE':
        genre.delete()
        return JsonResponse({'message': 'Gender successfully deleted'}, status=204,)