import os
import requests


def send_telegram(chat_id, message):
    """ Send messages to a Telegram chat """
    token = os.environ.get('TELEGRAM_TOKEN')
    requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    )
