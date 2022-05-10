from time import sleep

from main.models import FileModel
from . import BaseService


class LinesService(BaseService):

    def __init__(self, source_id: list, user_id: int):
        self.sources = self._get_source_by_id(source_id=source_id)
        self.group_name = f"user_{user_id}"
        self.user_id = user_id

    def __call__(self):
        self._notify_user(group_name=self.group_name, message="files accepted")
        files = []
        for inx, i in enumerate(self.sources, 1):
            file = i.file
            with file as f:
                sleep(3)
                self._notify_user(group_name=self.group_name, message=f"file{inx} start")
                cnt_line = len(f.readlines())
                sleep(5)
                files.append(
                    FileModel(
                        result=cnt_line,
                        is_edit=True,
                        user_id=self.user_id,
                        file=file
                    )
                )
                self._notify_user(group_name=self.group_name, message=f"file{inx} finish - count - {cnt_line}")
        self._create_main(files=files)
        self._notify_user(group_name=self.group_name, message=f"files finish!!!!!!!!")

    def _get_source_by_id(self, source_id: list) -> list[FileModel]:
        return FileModel.objects.filter(id__in=source_id)

    def _create_main(self, files: list[FileModel]) -> None:
        FileModel.objects.bulk_create(files)
