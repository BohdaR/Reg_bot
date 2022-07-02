import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import environ


env = environ.Env()
environ.Env.read_env(env_file='../.env')


API_TOKEN = env('TELEGRAM_API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def request_to_api(message):
    errors = ''
    responce = requests.post(
        url=env('ADD_USER_API'),
        data={
            "username": message.text.split()[0],
            "password": message.text.split()[1],
            "email": message.text.split()[2]
        })

    print(responce.status_code)
    if responce.status_code != 201:
        for el in responce.json().values():
            errors += str(el[0])
            return errors

    site_user_id = responce.json()['id']

    responce = requests.post(
        url=env('ADD_TELEGRAM_API'),
        data={
            "user_id": str(message.from_user.id),
            "name": f"{message.from_user.first_name} {message.from_user.last_name}",
            "username": message.from_user.username,
            "site_user": site_user_id
        })

    print(responce.status_code)
    if responce.status_code == 400:
        errors = "Ви уже зареєстровані за таками телеграм акаунтом"
        return errors

    return "Реєстрація успішна"


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hello {message.from_user.first_name}")
    await message.answer(f"Для реєстрації акаунта введіть логін, пароль і електронну пошту через пробіл")


@dp.message_handler()
async def echo(message: types.Message):

    if len(message.text.split()) == 3:   
        await message.answer(f"{await request_to_api(message)}")

    else:
        await message.answer(f"Перевірте коректність введених даних")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

