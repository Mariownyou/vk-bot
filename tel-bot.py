from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dp import dp, bot
from misc import ID_TEL
import datetime as dt
from time import sleep

time_to_send = dt.time(12)

class SetMessage(StatesGroup):
    waiting_for_message = State()


@dp.message_handler(commands="msg", state="*")
async def price_step_1(message: types.Message):
    await message.answer("Теперь напиши сообщение", reply_markup=types.ReplyKeyboardRemove())
    await SetMessage.next()

@dp.message_handler(state=SetMessage.waiting_for_message, content_types=types.ContentTypes.TEXT)
async def price_step_3(message: types.Message, state: FSMContext):
    await message.answer(f"теперь буду писать {message.text}", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    await message.answer('Напишите команду, потому что я не знаю что делать...')

async def echo(message='Все хорошо!'):
    await bot.send_message(ID_TEL, message)

while True:
    now = dt.datetime.now()
    if now.time == time_to_send:
        echo()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)