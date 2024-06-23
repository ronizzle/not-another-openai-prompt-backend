[install python](https://www.python.org/downloads/)

[install pip](https://pip.pypa.io/en/stable/installation/)

[install django](https://docs.djangoproject.com/en/5.0/topics/install/#installing-official-release)

install channels
`pip install channels`

install the openai library
`pip install openai`

install django-environ for loading `.env` file values:
`python -m pip install django-environ`

install django-cors headers:
`python -m pip install django-cors-headers`

[Get your key from OpenAPI](https://platform.openai.com/api-keys) (No more free tier T_T)

Copy .env_example to .env then define your OPENAI_API_KEY
`cp ./env_example .env`

Run the development server. This should be opened at 127.0.0.1:8000.
`python manage.py runserver`