from .models import Files, TypeFile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileSerializer, TypeFileSerializer


class ListFiles(APIView):
    def get(self, request):
        files = Files.objects.all()
        file_json = FileSerializer(files, many=True)
        return Response(file_json.data)

    def post(self, request):
        file_json = FileSerializer(data=request.data)  # Unmarshal
        if file_json.is_valid():
            file_json.save()
            return Response(file_json.data, status=201)
        return Response(file_json.errors, status=400)


class DetailFiles(APIView):
    def get(self, request, pk):
        file = Files.objects.get(pk=pk)
        file_json = FileSerializer(file)
        return Response(file_json.data, status=200)


class TypeFileAPI(APIView):
    def get(self, request):
        type_file = TypeFile.objects.all()
        type_file_json = TypeFileSerializer(type_file, many=True)
        return Response(type_file_json.data)