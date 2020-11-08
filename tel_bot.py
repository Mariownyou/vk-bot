import datetime as dt
import logging
import os
import time

import schedule
import telegram
from misc import TOKEN_TEL, ID_TEL
from vk_bot import sender

bot = telegram.Bot(token=TOKEN_TEL)

def send_message(message):
    return bot.send_message(chat_id=ID_TEL, text=message)

def job():
    sender()
    send_message('Все хорошо!')


schedule.every().day.at("12:00").do(job)
        

def main():
    logging.basicConfig(
        level=logging.INFO,
        filename='logs.log',
        format='%(asctime)s - %(message)s'
    )

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)

        except Exception as e:
            try:
                send_message(f'Бот упал с ошибкой: {e}')
            except:
                logging.exception(f'Бот упал с ошибкой: {e}')
                time.sleep(5)
            continue


if __name__ == '__main__':
    main()
