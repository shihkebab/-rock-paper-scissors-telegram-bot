from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, ContentType
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner
from additional_files.img_load import IMAGES_URL

router: Router = Router()


# Обработчик команды "/start"
@router.message(CommandStart())
async def process_command_start(msg: Message):
    await msg.answer_photo(photo=IMAGES_URL['preview'], caption=LEXICON_RU['/start'],
                           reply_markup=yes_no_kb)


# Обработчик команды "/help"
@router.message(Command(commands=['help']))
async def process_command_help(msg: Message):
    await msg.reply(LEXICON_RU['/help'], reply_markup=yes_no_kb)


# Хэндлер срабатывает если пользователь соглашается на игру
@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_yes_button(msg: Message):
    await msg.reply(LEXICON_RU['yes'], reply_markup=game_kb)


# Хэндлер срабатывает если пользователь отказывается от игры
@router.message(Text(text=LEXICON_RU['no_button']))
async def process_yes_button(msg: Message):
    await msg.reply(LEXICON_RU['no'], reply_markup=yes_no_kb)


# Главный игровой хэндлер
@router.message(Text(text=[LEXICON_RU['rock'],
                           LEXICON_RU['paper'],
                           LEXICON_RU['scissors']]))
async def process_game(msg: Message):
    bot_choice = get_bot_choice()
    await msg.answer_photo(photo=IMAGES_URL[bot_choice],
                           caption=f'{LEXICON_RU["bot_choice"]} 'f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(msg.text, bot_choice)
    await msg.answer(LEXICON_RU[winner], reply_markup=yes_no_kb)
