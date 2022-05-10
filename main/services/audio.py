from gtts import gTTS

from main.models import FileModel
from . import BaseService


class AudioService(BaseService):

    def __init__(
            self,
            text: str,
            user_id: int,
            lang: str = 'uk',
            slow: bool = False
    ):
        self.text = text
        self.lang = lang
        self.slow = slow
        self.group_name = f"user_{user_id}"

    def __call__(self, *args, **kwargs):
        self._notify_user(group_name=self.group_name, message="start process")
        FileModel().new(file=self.generate_audio())
        self._notify_user(group_name=self.group_name, message="finish")

    def generate_audio(self):
        self._notify_user(group_name=self.group_name, message="text covert to audio")
        return gTTS(text=self.text, lang=self.lang, slow=self.slow)
