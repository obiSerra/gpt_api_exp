import argparse
import json

from gpt_client.client import GptClient
from gpt_client.grimorium import generate_prompt_ita

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

    books = [
        "Harry Potter e la pietra filosofale",
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

        full_prompt = generate_prompt_ita(prompt)

        client.answer(full_prompt)
        # print(f"User: {client.last_propmpt()}")
        try:
            answer = json.loads(client.last_answer())
            if answer["incantesimo"].startswith("**"):
                print(
                    
                    f"[!]: Incantesimo inventato: {answer['incantesimo'].replace('**', '')}"
                )
            else:
                print(
                    f"""[!]: Incantesimo: {answer['incantesimo']} \n\n, 
Descrizione: {answer['descrizione']} \n\n,
Libro: {answer['libro']} \n\n, Usato da: {answer['usato da']}\n\n"""
                )

        except Exception as e:
            print(e)
            print(f"ERROR [!]: {client.last_answer()}")
            exit(0)
        # print(f"[>]: {answer}")
