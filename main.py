from aiogram import Bot, Dispatcher, executor, types
from translate import Translator
import logging
import requests

token = '5623017847:AAGgAhsgBn9jtpChRDE69C9C9cwMJb2IdFM'
logging.basicConfig(level=logging.INFO)

bot = Bot(token)
hey = Dispatcher(bot)
translator = Translator(from_lang = "en", to_lang="kk")


@hey.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.reply('Welcome to en-ru translator!\n' '\nWrite your text below 👇')


@hey.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.reply('@mqsd700 is my username, let me know if you have problems')


@hey.message_handler(content_types=['text'])
async def tr(message:types.Message):
    await message.reply(translator.translate(message.text))


if __name__ == '__main__':
    executor.start_polling(hey, skip_updates=True)