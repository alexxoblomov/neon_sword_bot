from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# main characters buttons
cross = InlineKeyboardButton(
    text='Крест',
    url='https://vampire-neon-sword.fandom.com/ru/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82'
)
babylon = InlineKeyboardButton(
    text='Вавилон',
    url='https://vampire-neon-sword.fandom.com/ru/wiki/%D0%92%D0%B0%D0%B2%D0%B8%D0%BB%D0%BE%D0%BD'
)
lily_storm = InlineKeyboardButton(
    text='Лили Шторм',
    url='https://vampire-neon-sword.fandom.com/ru/wiki/%D0%9B%D0%B8%D0%BB%D0%B8_%D0%A8%D1%82%D0%BE%D1%80%D0%BC'
)
alessandro_arrigo = InlineKeyboardButton(
    text='Алессандро Арриго',
    url='https://vampire-neon-sword.fandom.com/ru/wiki/%D0%90%D0%BB%D0%B5%D1%81%D1%81%D0%B0%D0%BD%D0%B4%D1%80%D0%BE_%D0%90%D1%80%D1%80%D0%B8%D0%B3%D0%BE'
)
nuna_clondyke = InlineKeyboardButton(
    text='Нуна Клондайк',
    url='https://vampire-neon-sword.fandom.com/ru/wiki/%D0%9D%D1%83%D0%BD%D0%B0_%D0%9A%D0%BB%D0%BE%D0%BD%D0%B4%D0%B0%D0%B9%D0%BA'
)
roberto_rivera = InlineKeyboardButton(
    text='Роберто Ривьера',
    url='https://vampire-neon-sword.fandom.com/ru/wiki/%D0%A0%D0%BE%D0%B1%D0%B5%D1%80%D1%82%D0%BE_%D0%A0%D0%B8%D0%B2%D1%8C%D0%B5%D1%80%D0%B0'
)
elvira_flores = InlineKeyboardButton(
    text='Эльвира Флорес',
    url='https://vampire-neon-sword.fandom.com/ru/wiki/%D0%AD%D0%BB%D1%8C%D0%B2%D0%B8%D1%80%D0%B0_%D0%A4%D0%BB%D0%BE%D1%80%D0%B5%D1%81'
)

# create inline-keyboard
via_dolorosa_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[elvira_flores, babylon, lily_storm],
                     [alessandro_arrigo, nuna_clondyke, roberto_rivera],
                     [cross]]
)


# boards buttons
miami_board = InlineKeyboardButton(
    text='Майами',
    url='https://www.owlbear.rodeo/room/td01o5bpvbT0/TheRubyAche'
)
washington_dc_board = InlineKeyboardButton(
    text='Вашингтон',
    url='https://www.owlbear.rodeo/room/42Q-LWhH7Jv1/TheUpsetMedal')

game_boards = InlineKeyboardMarkup(
    inline_keyboard=[[miami_board, washington_dc_board]]
)