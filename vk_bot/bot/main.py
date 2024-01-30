import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

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
    """Короче, пытался настроить нормально декоратор, но нифига не получилось. Какая была моя идея:
    def wrtieMessage(message,user_id,question,answers):
        @trackingStatusQuestion(question=question, answers=answers,message=message,user_id,user_id)
        def wm():
            ...
    То есть функция writeMessage будет принимать уже 4 аргумента, после чео все это идет в декоратор
    Но возникла проблема
    Функция wm должна принимать по любому какие-то параметры, чтобы отправить сообщение
    Но как она будет принимать аргументы, если она уже записана в другую функцию?((("""

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
