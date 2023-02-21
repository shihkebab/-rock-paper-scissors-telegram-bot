import random
from lexicon.lexicon_ru import LEXICON_RU


def get_bot_choice() -> str:
    return random.choice(['paper', 'rock', 'scissors'])


def _normalize_user_answer(user_answer: str) -> str:
    for i in LEXICON_RU:
        if LEXICON_RU[i] == user_answer:
            return i
        raise Exception


def get_winner(user_choice: str, bot_choice: str) -> str:  # доделать
    rule = {'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'}
    if bot_choice == user_choice:
        return 'nobody_won'
    elif rule[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'