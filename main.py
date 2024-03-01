from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os
import requests
import math

import datetime
import random as rnd
bot = Bot('6886210673:AAHF81QFFCDubHocI6hougqprluAGNjo5XQ')
dp = Dispatcher(bot=bot)


main_language = ReplyKeyboardMarkup(resize_keyboard=True)
main_language.add('Қазақша').add('Русский')


main_qazaq = ReplyKeyboardMarkup(resize_keyboard=True)
main_qazaq.add('Мен туралы').add('Программалау')
main_qazaq.add('Ойын').add('Ауа-рай').add('Рандомайзер')


main_programming_qazaq = ReplyKeyboardMarkup(resize_keyboard=True)
main_programming_qazaq.add('Python кітап').add('Курс').add('ООП').add('Алгоритмер').add('Деректер Қоры').add('Django')

main_generator_qaz = ReplyKeyboardMarkup(resize_keyboard=True)
main_generator_qaz.add('Құпия сөз жасау').add('PIN-код')


main_russian = ReplyKeyboardMarkup(resize_keyboard=True)
main_russian.add('Обо мне').add('Программирования')
main_russian.add('Игра').add('Погода').add('Рандом')

main_programming_russian = ReplyKeyboardMarkup(resize_keyboard=True)
main_programming_russian.add('Книга Python').add('Курс').add('ООП').add('Алгоритмы').add('База Данных').add('Django')

main_generator_russ = ReplyKeyboardMarkup(resize_keyboard=True)
main_generator_russ.add('Генерировать пароль').add('PIN-код')

@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMLZVttXQfatjvLKxZ856Oi7PIF7M8AAmsJAAIYQu4IE4mPShvxDM8zBA')
    await message.answer(f"{message.from_user.first_name}, Hello It's my first telegram bot!", reply_markup=main_language)

@dp.message_handler(text='Қазақша')
async def qazaq_language(message: types.Message):
    await message.answer('Сәлеметсіз бе. Қош келдіңіз!', reply_markup=main_qazaq)

@dp.message_handler(text='Мен')
async def me(message: types.Message):
    await message.answer('Сәлем, Мен болашақ жай ғана python developer')


@dp.message_handler(text='Ойын')
async def game(message: types.Message):
    await message.answer('Test1')

@dp.message_handler(text='Ауа-рай')
async def aua_rai(message: types.Message):
    await message.answer('Test1')



@dp.message_handler(text='Рандомайзер')
async def random(message: types.Message):
    await message.answer('Таңдаңыз:', reply_markup=main_generator_qaz)

@dp.message_handler(text='Құпия сөз жасау')
async def generator_qaz_mas(message: types.Message):
    pas = ''
    for i in range(16):
        pas = pas + rnd.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    await message.answer(pas, reply_markup=main_generator_qaz)

@dp.message_handler(text='PIN-код')
async def pin_kode4_qaz(message: types.Message):
    pas_pin_4 = ''
    for i in range(4):
        pas_pin_4 = pas_pin_4 + rnd.choice(list('1234567890'))
    await message.answer(pas_pin_4, reply_markup=main_generator_qaz)

@dp.message_handler(text='Python кітап')
async def qazaq_python_book(message: types.Message):
    await message.answer('Жақсылықтар: Көптеген код мысалдары; Материалдың өзектілігі; Жаттығулар.', reply_markup=main_programming_qazaq)
    await message.answer('Жамандықтар: Тапсырмалардың жауабтары жоқ.', reply_markup=main_programming_qazaq)
    await message.answer('https://vk.com/wall-54530371_309793', reply_markup=main_programming_qazaq)

@dp.message_handler(text='Курс')
async def qazaq_python_cours(message: types.Message):
    await message.answer('Егер сіз Python тілінде бағдарламалаудың жоғары сапалы, тегін және ең бастысы интеллектуалды курсын іздесеңіз, осы курсты таңдаңыз.', reply_markup=main_programming_qazaq)
    await message.answer('https://stepik.org/course/63085/promo', reply_markup=main_programming_qazaq)

@dp.message_handler(text='ООП')
async def qazaq_oop(message: types.Message):
    await message.answer('Курс атрибуттарды, әдістерді, қасиеттерді, сиқырлы әдістерді, мұрагерлік, полиморфизмді, класс декораторларын және т.б. қамтиды.''Курс теориялық және практикалық материалдармен, сондай-ақ тапсырмалармен 10 модульге бөлінген.', reply_markup=main_programming_qazaq)
    await message.answer('https://stepik.org/course/98974/promo', reply_markup=main_programming_qazaq)

@dp.message_handler(text='Алгоритмдер')
async def qazaq_algorytm(message: types.Message):
    await message.answer('Cұхбатқа дайындықты бағдарламалауға арналған онлайн платформа болып табылады. Бұл қызмет бағдарламалауды үйренгісі келетін пайдаланушыларға арналған кодтау және алгоритм тапсырмаларын ұсынады.', reply_markup=main_programming_qazaq)


@dp.message_handler(text='Деректер Қоры')
async def qazaq_db(message: types.Message):
    await message.answer('https://www.postgresql.org/', reply_markup=main_programming_qazaq)

@dp.message_handler(text='Django')
async def qazaq_django(message: types.Message):
    await message.answer('https://www.djangoproject.com/', reply_markup=main_programming_qazaq)

@dp.message_handler(text='Программалау')
async def programmer(message: types.Message):
    await message.reply('Теорияда теория мен практика ажырамас. Іс жүзінде бұлай емес.', reply_markup=main_programming_qazaq)


@dp.message_handler(text='Русский')
async def russian(message: types.Message):
    await message.answer('Здравствуйте, Добро пожаложать!', reply_markup=main_russian)

@dp.message_handler(text='Программирование')
async def russian(message: types.Message):
    await message.answer('В теории, теория и практика неразделимы. На практике это не так.', reply_markup=main_russian)

@dp.message_handler(text='Книга Python')
async def russian_book(message: types.Message):
    await message.answer('Достоинство: Множество примеров кода; Актуальность материала; Упражнения.', reply_markup=main_programming_russian)
    await message.answer('К задачам в книге нет ответов', reply_markup=main_programming_russian)
    await message.answer('https://vk.com/wall-54530371_309793', reply_markup=main_programming_russian)

@dp.message_handler(text='Курс')
async def russian_course(message: types.Message):
    await message.answer('Если вы ищете качественный, бесплатный и, самое главное, интеллектуальный курс по программированию на Python, выберите этот курс.', reply_markup=main_programming_russian)
    await message.answer('https://stepik.org/course/63085/promo', reply_markup=main_programming_russian)

@dp.message_handler(text='ООП')
async def russian_oop(message: types.Message):
    await message.answer('Класс атрибутов, специалисты, свойства, специалисты по магии, наследование, полиморфизм, класс декоратора и т. д. Камтида.»Теория и практика курса состояли из 10 модулей с материалами и заданиями.', reply_markup=main_programming_russian)

@dp.message_handler(text='База Данных')
async def russian_db(message: types.Message):
    await message.answer('https://www.postgresql.org/', reply_markup=main_programming_russian)

@dp.message_handler(text='Алгориты')
async def algoritm_russ(message: types.Message):
    await message.answer('это онлайн-платформа для программирования подготовки к собеседованию. Этот сервис предлагает задачи по кодированию и алгоритмам для пользователей, которые хотят изучить программирование.', reply_markup=main_programming_russian)

@dp.message_handler(text='Django')
async def russian_django(message: types.Message):
    await message.answer('https://www.djangoproject.com/', reply_markup=main_programming_russian)

@dp.message_handler(text='Обо мне')
async def russian_me(message: types.Message):
    await message.answer('Привет, я просто будущий разработчик Python.', reply_markup=main_russian)

@dp.message_handler(text='Игра')
async def russian_game(message: types.Message):
    await message.answer('Gamsw', reply_markup=main_russian)

@dp.message_handler(text='Погода')
async def russian_pogoda(message: types.Message):
    await message.answer('asdasd', reply_markup=main_russian)

@dp.message_handler(text='Рандом')
async def russian_random(message: types.Message):
    await message.answer('Выберите:', reply_markup=main_russian)

@dp.message_handler(text='Генерировать пароль')
async def generator_password_russ(message: types.Message):
    pas1 = ''
    for i1 in range(16):
        pas1 = pas1 + rnd.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    await message.answer(pas1, reply_markup=main_generator_russ)

if __name__ == '__main__':
    executor.start_polling(dp)




