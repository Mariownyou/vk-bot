from vk_api import VkApi, AuthError
from vk_api.utils import get_random_id
import datetime as dt
from misc import TOKEN_VK, ID_VK


# Vars
default_msg = 'ляля'
date = dt.datetime(2019, 10, 20)
now = dt.datetime.now()



class VkBot():
    def __init__(self, token):
        self.token = token
        self.default_msg = 'ляля\n'

        # vk vars
        vk_session = VkApi(token=self.token)
        self.vk = vk_session.get_api()
    
    def make_message(self):
        delta = now - date
        days_passed = delta.days
        msg = f'Поздравляю, прошло {days_passed} дней<3'
        return msg

    def send_message(self, msg=default_msg):
        self.vk.messages.send(user_id=ID_VK, message=msg, random_id=get_random_id())

    def run(self):
        msg = self.default_msg + self.make_message()
        self.send_message(msg)


def sender():
    vk = VkBot(TOKEN_VK)
    vk.run()


if __name__ == '__main__':
    sender()