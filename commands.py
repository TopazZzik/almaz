# Здесь что-то типа контроллера связывающий хендлеры и вью

from bot import bot
from aiogram import types
import random
import view
import model

game_model = model.GameData()


async def start(message: types.Message):
    await view.greetings(message)


async def play(message: types.Message):
    game_model.set_total_count(150)
    player1 = message.from_user.first_name
    player2 = 'first_almaz_bot'
    game_model.set_players([player1, player2])
    game_model.set_count(random.randint(0, 1))
    count = game_model.get_count()
    players = game_model.get_players()
    await view.message(message, f'В результате жеребьевки первым ходит игрок: {players[count]}.')
    if (count % 2) == 1:
        await bot_turn(message)
    else:
        await view.message(message, f'{players[0]}, возьмите конфеты:')


async def player_turn(message, num):
    await view.message(message, f'Вы взяли {num}')
    total_count = game_model.get_total_count()
    game_model.set_total_count(total_count - num)
    if await check_end(message):
        await bot_turn(message)


async def bot_turn(message):
    move = random.randint(1, 28)
    players = game_model.get_players()
    await view.message(message, f'{players[1]}: Я забираю {move} конфет!')
    total_count = game_model.get_total_count()
    game_model.set_total_count(total_count - move)
    if await check_end(message):
        await view.message(message, f'{players[0]}, возьмите конфеты:')


async def check_end(message):
    total_count = game_model.get_total_count()
    if total_count > 0:
        await view.message(message, f'Осталось {total_count} конфет!')
        count = game_model.get_count() + 1
        game_model.set_count(count)
        return True
    else:
        await view.message(message, 'Все конфеты разобраны.')
        count = game_model.get_count()
        players = game_model.get_players()
        await view.message(message, f'Победил игрок {players[count % 2]}!')
        game_model.restart()
        return False


async def finish(message: types.Message):
    game_model.restart()
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, '
                           f'до свидания!')


async def get_number(message: types.Message):
    if message.text.isdigit():
        number = int(message.text)
        if 0 < number < 29:
            await player_turn(message, number)
        else:
            await bot.send_message(message.from_user.id, f'Можно взять не более 28 конфет, переход хода.')
            await bot_turn(message)
    else:
        await bot.send_message(message.from_user.id, f'Вы ввели не число, переход хода.')
        await bot_turn(message)

    