from typing import Literal, NamedTuple

from moviepy.editor import VideoFileClip, concatenate_videoclips

from ..models import FileModel


ALLOWED_METHODS = Literal[
    'concatenate',
    'cut_video'
]


class VideoService(NamedTuple):
    user_id: int
    method: str
    videos: list[int]
    args: list[int] | None

    def __call__(self):
        getattr(self, self.method)()

    def concatenate(self):
        videos = self._get_videos_by_id(ids=self.videos)
        con_video = concatenate_videoclips([VideoFileClip(_.file.path) for _ in videos])

    def cut_video(self):
        video = self._get_videos_by_id(ids=self.videos)
        video = VideoFileClip(filename=video.file.path)
        new_video = video.subclip(*map(int, self.args))
        print(type(new_video))

    def _get_videos_by_id(self, ids: list[int]):
        videos = FileModel.objects.filter(id__in=ids)
        if self.method == 'cut_video':
            return videos.first()
        return videos
