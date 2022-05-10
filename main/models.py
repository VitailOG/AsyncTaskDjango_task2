import tempfile

from django.contrib.auth import get_user_model
from django.core.files import File
from django.db import models


User = get_user_model()


class FileModel(models.Model):
    file = models.FileField(upload_to='files/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_edit = models.BooleanField(default=False)
    result = models.CharField(verbose_name='Результат', max_length=32, null=True, blank=True)

    def __str__(self):
        return f"id - {self.id} is edit - {self.is_edit}"

    def new(self, *args, **kwargs):
        f1 = kwargs['file']
        with tempfile.TemporaryFile(mode='wb+') as f:
            f1.write_to_fp(f)
            file_name = '{}.mp3'.format('first')
            self.file.save(file_name, File(file=f))
        return super(FileModel, self).save()
