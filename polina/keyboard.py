from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

user_menu = ReplyKeyboardMarkup(resize_keyboard=True)
user_menu.row(KeyboardButton('Опросик😊'))
user_menu.row(KeyboardButton('альбом❤️'))

question1 = InlineKeyboardMarkup()
question1.row(InlineKeyboardButton(text='07.12.2022', callback_data="question1"))
question1.row(InlineKeyboardButton(text='07.01.2023', callback_data="question1"))
question1.row(InlineKeyboardButton(text='09.12.2022', callback_data="question2"))

question2 = InlineKeyboardMarkup()
question2.row(InlineKeyboardButton(text='02.11.2022', callback_data="question2_looz"))
question2.row(InlineKeyboardButton(text='07.01.2023', callback_data="question3"))
question2.row(InlineKeyboardButton(text='09.12.2022', callback_data="question2_looz"))

question3 = InlineKeyboardMarkup()
question3.row(InlineKeyboardButton(text='26.10.2005', callback_data="question4"))
question3.row(InlineKeyboardButton(text='02.11.2008', callback_data="question3_looz"))
question3.row(InlineKeyboardButton(text='25.10.2005', callback_data="question3_looz"))

question4 = InlineKeyboardMarkup()
question4.row(InlineKeyboardButton(text='Шоколадка', callback_data="question4_looz"))
question4.row(InlineKeyboardButton(text='Киндер', callback_data="question5"))
question4.row(InlineKeyboardButton(text='Коробка конфет', callback_data="question4_looz"))

question5 = InlineKeyboardMarkup()
question5.row(InlineKeyboardButton(text='Нет, ты че', callback_data="question5_looz"))
question5.row(InlineKeyboardButton(text='Да, конечно', callback_data="vin"))
