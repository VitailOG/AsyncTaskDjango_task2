from rest_framework import serializers

from main.models import FileModel


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
