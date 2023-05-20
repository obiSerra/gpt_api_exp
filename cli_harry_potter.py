import openai

import argparse


class GptClient:
    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        self.message_history = []
        self.full_history = []
        self.model = model
        openai.api_key = open("key.txt", "r").read().strip("\n")

    def answer(self, prompt: str, role: str = "user"):
        self.message_history.append({"role": role, "content": prompt})

        completion = openai.ChatCompletion.create(
            model=args.model, messages=self.message_history
        )

        message = completion["choices"][0]["message"]

        self.full_history.append(completion)
        self.message_history.append(message)

    def last_propmpt(self):
        return self.message_history[-2]["content"]

    def last_answer(self):
        return self.message_history[-1]["content"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate code from a prompt")

    parser.add_argument(
        "--model",
        dest="model",
        type=str,
        default="gpt-3.5-turbo",
        help="the model to use",
    )

    parser.add_argument(
        "--output", dest="output", type=str, default="", help="the output file to use"
    )

    args = parser.parse_args()


    client = GptClient(model=args.model)

    books = ["Harry Potter e la pietra filosofale",
    "Harry Potter e la camera dei segreti",
    "Harry Potter e il prigioniero di Azkaban",
    "Harry Potter e il calice di fuoco",
    "Harry Potter e l'Ordine della Fenice",
    ]
# Harry Potter e il principe mezzosangue


    # base_prompt = f"""
    # Il tuo compito è quello di generare una citazione tratta da uno dei seguenti libri della saga di Harry Potter: {','.join(books)}.
    # Il formato della risposta deve essere delimitato da triple backticks (```) e deve avere il seguente formato:
    # citazione: <citazione>
    # personaggio: <personaggio>
    # libro: <libro>
    # """
    while True:
        prompt = input("[?] Un incantesimo per: ")

        base_prompt = f"""
        Il tuo compito è quello di generare il nome di un incantesimo tratto dai libri della saga di Harry Potter per eseguire l'azione delimitata da riple backticks (```).
        Il formato della risposta deve avere il seguente formato:
        incantesimo: <nome dell'incantesimo>
        descrizione: <descrizione dell'incantesimo>


        ```{prompt}```
        """


        client.answer(base_prompt)
        # print(f"User: {client.last_propmpt()}")
        print(f"[>]: {client.last_answer()}")
