from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards.inline_buttons import via_dolorosa_keyboard, game_boards
from lexicon.lexicon import LEXICON_RU

# init router
router = Router()


# /start handler
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='viadolorosa'))
async def send_main_pack(message: Message):
    await message.answer(text='Члены стаи "Via Dolorosa"', reply_markup=via_dolorosa_keyboard)


@router.message(Command(commands='gameboards'))
async def send_game_boards(message: Message):
    await message.answer(text='Локации, где проходит игра', reply_markup=game_boards)