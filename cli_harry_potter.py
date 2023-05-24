import argparse
import json

from gpt_client.client import GptClient
from gpt_client.grimorium import generate_prompt, generate_prompt_ita

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate code from a prompt")

    parser.add_argument(
        "--model",
        dest="model",
        type=str,
        default="gpt-3.5-turbo",
        help="the model to use",
    )

    parser.add_argument("--output", dest="output", type=str, default="", help="the output file to use")

    args = parser.parse_args()

    client = GptClient(model=args.model)

    system_prompt = generate_prompt()
    client.system_prompt(system_prompt)

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
        prompt = input("[?] A spell for: ")

        full_prompt = """```{prompt}```"""

        client.answer(full_prompt)
        print("\n\n")
        # print(f"User: {client.last_propmpt()}")
        try:
            answer = client.last_answer()
            if answer == "nessun incantesimo trovato":
                print(f"[!]: {answer_data}")
                break

            answer_data = json.loads(answer)
            print(f"[!]: Incantesimo: {answer_data['spell']}\n")
            print(f"     Descrizione: {answer_data['description']}")
            print(f"     Esempio: {answer_data['example']}")
            print(f"     Usato_da: {answer_data['used_by']}")
            print(f"     Libro: {answer_data['book']}")
            print("\n\n")

        except Exception as e:
            print(e)
            print(f"ERROR [!]: {client.last_answer()}")
            
        # print(f"[>]: {answer}")
