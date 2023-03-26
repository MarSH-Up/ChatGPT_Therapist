from Api_callback import send_prompt
import twilo


if __name__ == '__main__':
    prompt = input()
    response = send_prompt(prompt)
    print(response)
