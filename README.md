# AshLog

Open Source API and web app to handle logs with ease.

<a href="https://liberapay.com/AshLog/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a>

## Sample usage

Once you have the server up and running, you have to create an account and generate a token. Then you can send requests to the API directly from your codebase.

### Examples 
#### JavaScript example

```javascript
import axios from 'axios';

axios({
    method: 'POST',
    url: 'http://localhost:8000/api/log/',
    body: {
        project: projectID,
        event: 'Hello World!',
    },
    headers: {
        Authorization: `Bearer ${token}`,
    },
});

```

#### Python example

```python
import requests

headers = {
    'Authorization': f'Bearer {token}',
}

data = {
    'project': project_id,
    'event': 'Hello World!',
}

requests.post(
    'http://localhost:8000/api/log/',
    json=data,
    headers=headers,
)
```

### Trigger actions

When a request is sent you can also trigger one or more actions. For instance, you can send a telegram message with the event as text using the `send_telegram` action:

```python
import requests

headers = {
    'Authorization': f'Bearer {token}',
}

data = {
    'project': project_id,
    'event': 'Hello World!',
    'actions': [
        {
            'action': 'send_telegram',
            'args': {
                'chat_id': telegram_chat_id,
            },
        },
    ],
}

requests.post(
    'http://localhost:8000/api/log/',
    json=data,
    headers=headers,
)
```

In this case you should set a TELEGRAM_TOKEN environment variable with your Telegram bot token. 

## Installation

The easiest way to run AshLog is using a Docker container.

1. Clone this repository

    ```
    $ git clone https://github.com/ashlog-rest/ashlog
    ```

2. Create `.env` file and set the requirred environment variables as stated in the <a href="https://github.com/ashlog-rest/ashlog#developer-instructions">Developer Instructions</a>.

3. Make sure you have docker installed and run:

    ```
    $ docker-compose up --build  
    ```

That's it! Now you should be able to access the REST API and the webapp on http://localhost:8000/.

## Developer Instructions

1. Is it recommended to create a virtual environment

    ```
    $ python -m venv .venv
    ```

2. Enter the virtual environment

    ```
    $ source .venv/bin/activate
    ```

3. Install dependencies

    ```
    $ pip install -r requirements.txt
    ```

4. Set env variables

- Create a .env file

  ```
  $ touch .env
  ```

- Set env variables inside the file

  ```
  DJANGO_SECRET_KEY='your secret key'
  FIELD_ENCRYPTION_KEY='your encription key'
  ```

  That's how you can generate Django secret keys:

  ```
  $ python manage.py shell
  ```

  ```python
  from django.core.management.utils import get_random_secret_key

  get_random_secret_key()
  ```

  The encryption key can be generated like that:

  ```python
  import os
  import base64

  new_key = base64.urlsafe_b64encode(os.urandom(32))
  print(new_key)
  ```

5. Run server

    ```
    $ python manage.py runserver
    ```

6. (Optional) Create a superuser in order to use the django admin site

    ```
    $ python manage.py createsuperuser
    ```