from pathlib import Path

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import FileModel
from main.services.video import ALLOWED_METHODS


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileModel
        fields = "__all__"

    def create(self, validated_data):
        files = FileModel.objects.bulk_create(
            [FileModel(file=_) for _ in self.context]
        )
        return [_.id for _ in files]


class AudioSerializer(serializers.Serializer):
    text = serializers.CharField()
    lang = serializers.CharField(allow_null=True)
    slow = serializers.BooleanField(default=False)


class VideoSerializer(serializers.Serializer):
    video = serializers.FileField()
    method = serializers.CharField()
    args = serializers.ListField(
        child=serializers.IntegerField(),
        min_length=1,
        max_length=2,
        required=False
    )

    LENGTH_ARGUMENTS_FOR_METHOD = {
        'concatenate': 0,
        'cut_video': 2
    }

    def validate(self, attrs):
        if self.LENGTH_ARGUMENTS_FOR_METHOD[attrs['method']] != len(attrs.get('args', [])):
            raise Exception
        return attrs

    def validate_method(self, value):
        if value.lower() in ('concatenate', 'cut_video'):
            return value
        raise ValidationError("Method not supported")

    def validate_video(self, value):
        suffix = Path(value.name).suffix
        if suffix != '.mp4':
            raise ValidationError("File not video")
        return value

    def create(self, validated_data):
        files = FileModel.objects.bulk_create(
            [FileModel(file=_) for _ in self.context]
        )
        return [_.id for _ in files]
