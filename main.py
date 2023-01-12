import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5898528790:AAEua2zAAMOTORdKWiDasA47LXFhNZBV7R8'
wikipedia.set_lang("uz")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Assalomu alaykum, " + message.from_user.full_name +"! " + "\nMen Wikipedia Botman. \n Wikipediadan qidirish uchun kalit so`z yuboring, masalan : Toshkent\nAdmin: "
                                                           "@Intelligentt_01")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        resp = wikipedia.summary(message.text)
        await message.reply(resp)
    except:
        await message.answer("Bu kalit so`zga doir maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
