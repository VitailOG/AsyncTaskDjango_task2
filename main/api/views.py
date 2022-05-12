from rest_framework import views, response, generics
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import FileSerializer, AudioSerializer, VideoSerializer
from main.models import FileModel
from main.tasks import execute_file, audio, video


class MainApi(generics.GenericAPIView, views.APIView):

    queryset = FileModel.objects
    parser_classes = (FormParser, MultiPartParser)

    def get(self, request):
        files = FileModel.objects.all()
        return response.Response(
            data=self.get_serializer_class()(files, many=True).data
        )

    def post(self, request):
        s = FileSerializer(data=request.data, context=request.data.getlist('file', []))
        s.is_valid(raise_exception=True)
        s.save()
        execute_file.delay(s.instance, user_id=request.user.id)
        return response.Response({"create": True})

    def get_serializer_class(self):
        return FileSerializer


class AudioApi(generics.GenericAPIView, views.APIView):

    serializer_class = AudioSerializer

    def post(self, request):
        audio.delay(user_id=request.user.id, **request.data)
        return response.Response({"audio": True})


class VideoApi(generics.GenericAPIView, views.APIView):

    serializer_class = VideoSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        s = self.get_serializer_class()(data=request.data, context=request.data.getlist('video', []))
        s.is_valid(raise_exception=True)
        s.save()
        video.delay(
            user_id=request.user.id,
            source_id=s.instance,
            method=request.data['method'],
            args=self.request.data.getlist('args', [])
        )
        return response.Response({"video": True})
