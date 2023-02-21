from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()


# Обрабатываем рандомные сообщения
@router.message()
async def router_message_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])