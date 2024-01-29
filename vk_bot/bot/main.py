import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def writeMessage(message: str, user_id: int):
    vk.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": get_random_id(),
    })


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message_user = event.text.lower()
        user_id = event.user_id
        if message_user == 'пока':
            message = 'Пока'
            writeMessage(message, user_id)
            exit()
        else:
            message = message_user
            writeMessage(message, user_id)
