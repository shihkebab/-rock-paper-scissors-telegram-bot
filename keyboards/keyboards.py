from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" "Не хочу!"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем в билдер параметр row с шириной 2
yes_no_kb_builder.row(button_yes, button_no, width=2)
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True,
                                        )

# ------- Создаем игровую клавиатуру без билдера -------

# создаем кнопки игровой клавиатуры
button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_rock], [button_scissors], [button_paper]],
                                                   resize_keyboard=True)
