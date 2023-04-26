import openai

openai.api_key = open("key.txt", "r").read().strip("\n")


class GptClient:

    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.message_history = []
        self.model = model


    def user_prompt(self, prompt: str):
        self.message_history.append({"role": "user", "content": f"{prompt}"})

    def completion(self):
        completion = openai.ChatCompletion.create(model=self.model, messages=self.message_history)
        self.message_history.append(completion["choices"][0]["message"])
    
    def assistant_response(self):
        print(self.message_history)
        return self.message_history[-1]["content"]

