from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_openai_answer(question):
    response = send_openai_question(question)
    return format_openai_response(response)


def send_openai_question(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"""\"{question}\""""
        }],
        temperature=0.8,
        max_tokens=1000
    )
    return response


def format_openai_response(response):
    return response.choices[0].message.content.strip()

def generate_realtime_openai_answer(question):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"""\"{question}\""""
        }],
        temperature=0.8,
        max_tokens=1000,
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            yield content

