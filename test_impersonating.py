import openai

openai.api_key = open("key.txt", "r").read().strip("\n")


def generate_dialog():
    message_history = []

    first_input = 'Presentati come "Carlo la ballerina" un AI personal assistant'

    message_history.append({"role": "user", "content": f"{first_input}"})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message_history)

    print(completion)
    message_history.append(completion["choices"][0]["message"])

    print(message_history[-1])


if __name__ == "__main__":
    generate_dialog()
