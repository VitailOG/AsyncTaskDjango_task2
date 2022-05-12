from celery import shared_task

from main.services.file import LinesService
from main.services.audio import AudioService
from main.services.video import VideoService


@shared_task
def execute_file(source_id: list, user_id: int):
    LinesService(source_id=source_id, user_id=user_id)()


@shared_task
def audio(user_id: int, text: str, lang: str, slow: bool):
    AudioService(text=text, lang=lang, slow=slow, user_id=user_id)()


@shared_task
def video(user_id: int, source_id: list, method: str, args: list[int]):
    VideoService(user_id=user_id, videos=source_id, method=method, args=args)()
