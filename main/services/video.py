from typing import Literal, NamedTuple

from moviepy.editor import VideoFileClip, concatenate_videoclips


ALLOWED_METHODS = Literal[
    'concatenate',
    'cut_video'
]


class VideoService(NamedTuple):
    user_id: int
    method: ALLOWED_METHODS
    videos: list

    def __call__(self, *args, **kwargs):
        pass

    def concatenate(self):
        return concatenate_videoclips(self.videos)

    def cut_video(self):
        pass


# from moviepy.editor import VideoFileClip, concatenate_videoclips
#
# v1 = VideoFileClip('videoplayback.mp4')
# v2 = VideoFileClip('Tanks fire in streets of Mariupol, Ukraine.mp4')
#
# v = v1.subclip(3, 10)
# common = concatenate_videoclips([v1, v2])
# print(v1.duration)
# print(v2.duration)
# print(common.duration)
