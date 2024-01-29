import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

token = "vk1.a.37ibOrx473bf_-I-FmFpB-o455I-gXn-s6B4m6eMfd-qgLsPeXRZOH7q-l4kPDJ3RivHDu4gKe75OVLaeGX5aVPrWiyBJb4lTLr3xOwWo1-fnH12ybk85xb6IEBLxwszSfjnuzGQ1_V32BkqDc6x6CEL4TL56Oekik6SsSbv7LGzAO5F6hu1MYqKoJA-VgWbXPaZfXyaxwt2aXycg21FQg"

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


class FSM(object):
    def __init__(self):
        self.now_state = ""
        self.question = 'question'
        self.answer = 'answer'
        self.expectation = 'expectation'

    def questions(self):
        return self.question

    def answers(self):
        return self.answer

    def expectations(self):
        return self.expectation


def trackingStatusQuestion(question: str, answers: list):
    message_1 = ''
    if len(question) > 0 and len(answers) > 0:
        message_1 = question + '\n'
        for index, answer in enumerate(answers):
            message_1 += str(index + 1) + ")" + str(answer) + "\n"

    def func_decorator(func):
        def trackStatus(message, user_id, *args, **kwargs):
            if len(message_1) > 0:
                func(message_1, user_id, *args, **kwargs)
            else:
                func(message, user_id, *args, **kwargs)

        return trackStatus

    return func_decorator


question: str = ''
answers: list = []


@trackingStatusQuestion(question=question, answers=answers)
def writeMessage(message, user_id):
    vk.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": get_random_id(),
    })
    print("Я написал такое сообщение: ", message)


def sendImage(user_id: str, photo: str):
    vk.method("messages.send", {
        "user_id": user_id,
        "attachment": "".join(photo),
        "random_id": get_random_id(),
    })


fsm = FSM()
fsm.now_state = fsm.expectations()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message_user = event.text.lower()
        user_id = event.user_id
        if message_user == 'пока':
            message = 'Пока'
            writeMessage(message, user_id)
            exit()
        # elif message_user == "начать викторину":
        #     message = """Начинаем. Итак, первый вопрос:
        #     Что изображено на картинке?"""
        #     fsm.now_state = fsm.questions()
        else:
            question += "shgakjc"
            message = message_user
            writeMessage(message, user_id)
