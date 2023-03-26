import openai
from Credential_extraction import ApiKey

openai.api_key = ApiKey()


def send_prompt(content_message):
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]
    messages.append({"role": "user", "content": content_message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    response_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_content})

    return response_content
