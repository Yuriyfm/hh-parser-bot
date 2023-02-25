import requests
import json
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import os
from telegramBot import bot

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
CHAT_ID = os.getenv("CHAT_ID")
# hh_React_Vacancies_bot
bot_token = os.getenv("TELEGRAM_TOKEN")
DATA = []


def is_new(post):
    if post['id'] in DATA:
        return False
    DATA.append(post['id'])
    try:
        bot.send_message(int(CHAT_ID), f'Название: {post["name"]}\n'
                                       f'Работодатель: {post["employer"]["name"]}\n'
                                       f'Локация: {post["area"]["name"]}\n'
                                       f'Опубликована: {post["published_at"]}\n'
                                       f"Обязательные требования: {post['snippet']['requirement']}\n" 
                                       f'Ссылка: {post["alternate_url"]}')
    except Exception as e:
        print(e)
    time.sleep(1)
    return True


def getPage(page=0):

    params = {
        'text': 'Frontend React',
        'schedule': 'remote',
        'experience': 'between1And3',
        'period': '3',
        'page': page,
        'per_page': 100
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()  # Декодируем ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


def main():
    while True:
        for page in range(0, 20):
            try:
                jsObj = json.loads(getPage(page))
                if jsObj['items']:
                    for i in jsObj['items']:
                        is_new(i)

                if (jsObj['pages'] - page) <= 1:
                    break

            except Exception as e:
                bot.send_message(int(CHAT_ID), f'бот упал с ошибкой: {repr(e)}')
                print(e)
                exit()
        time.sleep(60)


# блок main
if __name__ == '__main__':
    main()
    bot.polling()

