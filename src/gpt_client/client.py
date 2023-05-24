import openai


class GptClient:
    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        self.message_history = []
        self.full_history = []
        self.model = model
        openai.api_key = open("key.txt", "r").read().strip("\n")

    def system_prompt(self, prompt: str):
        self.message_history.append({"role": "system", "content": prompt})

    def answer(self, prompt: str, role: str = "user"):
        self.message_history.append({"role": role, "content": prompt})

        completion = openai.ChatCompletion.create(model=self.model, messages=self.message_history)

        message = completion["choices"][0]["message"]

        self.full_history.append(completion)
        self.message_history.append(message)

    def last_propmpt(self):
        return self.message_history[-2]["content"]

    def last_answer(self):
        return self.message_history[-1]["content"]
