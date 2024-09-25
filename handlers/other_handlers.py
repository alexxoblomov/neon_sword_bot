import random
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from handlers import characters_list
from lexicon.lexicon import LEXICON_TECHNICAL_RU

# init router
router = Router()


# init states
class Form(StatesGroup):
    waiting_for_character = State()
    waiting_for_attributes = State()


# dice values func
def generate_dice_values(character, attribute_1, attribute_2=None):
    # character check
    if character not in characters_list.characters:
        print("Персонаж не найден!")
        return

    # get attributes
    attributes = characters_list.characters[character]

    # check attributes
    if attribute_1 not in attributes:
        print("Первый атрибут не найден!")
        return

    if attribute_2 and attribute_2 not in attributes:
        print("Второй атрибут не найден!")
        return

    # get number of dices
    total = attributes[attribute_1]

    if attribute_2:
        total += attributes[attribute_2]  # Добавляем второй атрибут только если он существует

    # generate dices value
    random_values = [random.randint(1, 10) for _ in range(total)]

    return random_values


@router.message(Command("roll"))
async def start_roll(message: Message, state: FSMContext):
    await message.answer(LEXICON_TECHNICAL_RU["enter_character"])
    await state.set_state(Form.waiting_for_character)


@router.message(Form.waiting_for_character)
async def process_character(message: Message, state: FSMContext) -> None:
    character = message.text.strip()

    if character in characters_list.characters:
        await state.update_data(character=character)
        await message.answer(LEXICON_TECHNICAL_RU["enter_attributes"])
        await state.set_state(Form.waiting_for_attributes)
    else:
        await message.answer(LEXICON_TECHNICAL_RU["character_not_found"])


@router.message(Form.waiting_for_attributes)
async def process_attributes(message: Message, state: FSMContext) -> None:
    attributes = message.text.strip().split()

    if len(attributes) not in [1, 2]:
        await message.answer(LEXICON_TECHNICAL_RU["incorrect_attributes_format"])
        return

    data = await state.get_data()
    character = data.get("character")

    attribute_1 = attributes[0]
    attribute_2 = attributes[1] if len(attributes) == 2 else None
    dice_values = generate_dice_values(character, attribute_1, attribute_2)

    # output
    if dice_values is not None:
        message_text = f"Броски для {character} на {attribute_1}"
        if attribute_2:
            message_text += f" и {attribute_2}"
        message_text += f": \n" + ', '.join(map(str, dice_values))

        await message.answer(message_text, parse_mode=ParseMode.MARKDOWN)
    else:
        await message.answer(LEXICON_TECHNICAL_RU["error_generating_roll"])

    await state.set_state(None)
