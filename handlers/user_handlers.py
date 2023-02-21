from aiogram import Router
from aiogram.filters import Command, CommandStart, text
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner


router: Router = Router()


@router.message(CommandStart)
async def process_command_start(msg: Message):
    await msg.answer(LEXICON_RU['/start'], reply_markup=yes_no_kb)


@router.message(Command['help'])
async def process_command_help(msg: Message):
    await msg.reply(LEXICON_RU['/help'], reply_markup=yes_no_kb)