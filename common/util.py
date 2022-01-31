import requests


def send_discord(channel_id, token, message):
    botToken = 'OTMzNjc5MjExMjQyMjIxNjI4.YelChg.AcU1f4X2LX7s_pwHCF4Y5O7fTkE'
    baseURL = f'https://discordapp.com/api/channels/{channel_id}/messages'
    headers = {
        'Authorization': f'Bot {token}',
        'User-Agent': 'AshLog',
        'Content-Type': 'application/json',
    }
    requests.post(baseURL, headers=headers, json={'content': message})


def send_telegram(chat_id, token, message):
    """ Send messages to a Telegram chat """
    requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    )


def send_post_request(url, data, headers=None):
    """ Send POST request """
    requests.post(url, json=data, headers=headers)
