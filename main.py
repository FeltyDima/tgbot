import keyboard as kb
from texts import *
from config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.input_media import InputMedia
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветик, любимая🥰 Выбери категорию!', reply_markup=kb.user_menu)



# !!!ОПРОС!!!
@dp.message_handler(text='Опросик😊')
async def contact(message: types.Message):
    await bot.send_message(message.from_user.id, text=question1_text, reply_markup=kb.question1)

@dp.callback_query_handler(text="question1")
async def question1(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question1_1_text, reply_markup=kb.question1)


@dp.callback_query_handler(text="question2")
async def question2(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question2_text, reply_markup=kb.question2)

@dp.callback_query_handler(text="question2_looz")
async def question2(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question2_1_text, reply_markup=kb.question2)


@dp.callback_query_handler(text="question3")
async def question3(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question3_text, reply_markup=kb.question3)

@dp.callback_query_handler(text="question3_looz")
async def question3(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question3_1_text, reply_markup=kb.question3)


@dp.callback_query_handler(text="question4")
async def question4(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question4_text, reply_markup=kb.question4)

@dp.callback_query_handler(text="question4_looz")
async def question4(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question4_1_text, reply_markup=kb.question4)


@dp.callback_query_handler(text="question5")
async def question5(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question5_text, reply_markup=kb.question5)

@dp.callback_query_handler(text="question5_looz")
async def question5(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=question5_1_text, reply_markup=kb.question5)


@dp.callback_query_handler(text="vin")
async def vin(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=vin_text)
    await callback.message.answer_document(open('serds.exe', 'rb'))

# !!!АЛЬБОМ!!!


fruits_callback = CallbackData('Fruits', 'page')

def get_fruits_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    has_next_page = len(fruits) > page + 1

    if page != 0:
        keyboard.add(InlineKeyboardButton(
            text = "< Назад",
            callback_data=fruits_callback.new(page = page - 1)
        ))   
    
    keyboard.add(
        InlineKeyboardButton(
            text=f"{page + 1} / 43",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.add(
            InlineKeyboardButton(
                text="Вперед >",
                callback_data=fruits_callback.new(page=page+1)
            )
        )

    return keyboard

@dp.message_handler(text='альбом❤️')
async def fruits_index(message: types.Message):
    fruit_data = fruits[0]
    keyboard = get_fruits_keyboard()
    photo = open(f"{fruit_data.get('image_url')}", 'rb')

    await message.answer_photo(photo=photo, reply_markup=keyboard)

@dp.callback_query_handler(fruits_callback.filter())
async def fruit_page_handler(query: types.CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))

    fruit_data = fruits[page]
    keybord = get_fruits_keyboard(page)

    photo = InputMedia(type = "photo", media=open(f"{fruit_data.get('image_url')}", 'rb'))

    await query.message.edit_media(photo, keybord)


executor.start_polling(dp, skip_updates=True)