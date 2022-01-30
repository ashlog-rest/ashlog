import os
import requests


def send_telegram(chat_id, token, message):
    """ Send messages to a Telegram chat """
    requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    )
