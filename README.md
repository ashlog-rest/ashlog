# AshLog

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