from vk_api import VkApi, AuthError
from vk_api.utils import get_random_id
import datetime as dt
from misc import TOKEN_VK, ID_VK



# Vars
default_msg = 'ляля'
date = dt.datetime(2019, 10, 20)
now = dt.datetime.now()
time_send = dt.time(12)

print(date, now, time_send)


def make_message():
    delta = now - date
    days_passed = delta.days
    msg = f'Поздравляю, прошло {days_passed} <3'
    return msg


class VKBot():
    def __init__(self, token):
        self.token = TOKEN_VK
        self.default_msg = 'ляля'

        # vk vars
        vk_session = VkApi(token=TOKEN_VK)
        try:
            vk_session.auth(token_only=True)
        except AuthError as error_msg:
            print(error_msg)

        self.vk = vk_session.get_api()
    
    def make_message(self):
        delta = now - date
        days_passed = delta.days
        msg = f'Поздравляю, прошло {days_passed} <3'
        return msg

    def send_message(self, msg=default_msg):
        self.vk.messages.send(user_id=ID_VK, message=msg, random_id=get_random_id())
