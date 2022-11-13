from aiogram import types
from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n Это игра в конфетки\n На столе лежит 150 конфет.\n Играют два игрока, делая ход друг после друга.\n Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более чем 28 конфет.\n Все конфеты оппонента достаются сделавшему последний ход.\n Сколько конфет нужно взять первому игроку,\n чтобы забрать все конфеты у своего конкурента?\n Для начала игры введите команду /play')


async def message(message, text):
    await bot.send_message(message.from_user.id, text)