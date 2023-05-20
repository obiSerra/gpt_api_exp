from gpt_client.client import GptClient


def generate_prompt_ita(suggestion: str):
    base_prompt = f"""
        Il tuo compito è quello di suggerire il nome di un incantesimo tratto dall'universo fantasico di Harry Potter 
        per eseguire l'azione delimitata da triplici backticks (```). \
        Se non esiste un incantesimo per l'azione richiesta inventane uno; in questo caso usa un doppio asterisco (**)
        che l'incantesimo e' sato inventato.
        La risposta deve essere in formato JSON con le seguenti chiavi:
        incantesimo: <nome dell'incantesimo>
        descrizione: <descrizione dell'incantesimo>
        libro: <libro>
        usato da: <personaggio>


        ```{suggestion}```
        """
    return base_prompt