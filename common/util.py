import os
import requests
import requests


def send_telegram(chat_id, token, message):
    """ Send messages to a Telegram chat """
    requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    )


def send_post_request(url, data, headers=None):
    """ Send POST request """
    requests.post(url, json=data, headers=headers)
