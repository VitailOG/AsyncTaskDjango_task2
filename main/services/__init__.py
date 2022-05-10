import channels.layers
from asgiref.sync import async_to_sync

from main.models import FileModel


class BaseService:

    def _notify_user(self, group_name: str, message: str) -> None:
        layer = channels.layers.get_channel_layer()

        async_to_sync(layer.group_send)(
            group_name,
            {
                'type': 'notify',
                'message': message
            }
        )

