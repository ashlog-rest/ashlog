# AshLog

Open Source API and web app to handle logs with ease.

<a href="https://liberapay.com/AshLog/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ashlog-rest/ashlog)

## Documentation

Read the documentation on: [https://ashlog.readthedocs.io](https://ashlog.readthedocs.io/).

## Examples

### JavaScript example

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

### Python example

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