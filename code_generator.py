import openai

openai.api_key = open("key.txt", "r").read().strip("\n")


def generate_code():
    message_history = []

    pre_settings = """You are a code generator AI, you will generate the requested code without providing any other information or status messages.
    Answer Yes if you understand the request, otherwise answer No.
    """
    message_history.append({"role": "user", "content": f"{pre_settings}"})
    message_history.append({"role": "assistant", "content": "Yes"})

    first_input = "Give me an example of "

    value = "a terraform configuration with a google cloud function as the only resource"

    message_history.append({"role": "user", "content": f"{first_input} {value}"})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message_history)

    response = completion["choices"][0]["message"]["content"]
    print(response)

    with open("generated_code_1.txt", "w") as f:
        f.write(str(response))


if __name__ == "__main__":
    generate_code()
