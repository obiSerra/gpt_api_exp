from gpt_client.client import GptClient


def generate_prompt_ita(suggestion: str):
    base_prompt = f"""Il tuo compito è quello di suggerire il nome di un incantesimo tratto dall'universo fantasico \
di Harry Potter per eseguire l'azione delimitata da triplici backticks (```); se non esiste un incantesimo adatto \
rispondi solo con 'nessun incantesimo trovato'.
La risposta deve essere in formato JSON con le seguenti chiavi:
incantesimo: <nome dell'incantesimo>
esempio: <esempio di utilizzo>
descrizione: <descrizione dell'incantesimo>
libro: <libro>
usato_da: <personaggio>

Suggerisci un incantesimo per:
```{suggestion}```"""
    return base_prompt


def generate_prompt():
    base_prompt = f"""Your task is to suggest the name of a spell from the Harry Potter fantasy universe to perform the \
action delimited by triple backticks (```); if there is no suitable spell respond with an empty JSON object.
The answer must be in JSON format with the following keys:
spell: <spell name>
example: <example of use>
description: <spell description>
book: <book>
used_by: <character>
"""
    return base_prompt


def generate_prompt_ita_(suggestion: str):
    base_prompt = f"""Il tuo compito è quello di suggerire il nome di un incantesimo tratto dall'universo fantasico \
di Harry Potter per eseguire l'azione delimitata da triplici backticks (```); se non esiste un incantesimo per \
l'azione richiesta inventane uno: in questo caso delimita con un doppio asterisco (**) il nome.
La risposta deve essere in formato JSON con le seguenti chiavi:
incantesimo: <nome dell'incantesimo>
descrizione: <descrizione dell'incantesimo>
libro: <libro>
usato_da: <personaggio>

Suggerisci un incantesimo per:
```{suggestion}```"""
    return base_prompt

    base_prompt = f"""Il tuo compito è quello di suggerire il nome di un incantesimo tratto dall'universo fantasico \
di Harry Potter per eseguire l'azione delimitata da triplici backticks (```); solo se non esiste un incantesimo per \
l'azione richiesta inventane uno: in questo caso delimita con un doppio asterisco (**) il nome.
La risposta deve essere in formato JSON con le seguenti chiavi:
incantesimo: <nome dell'incantesimo>
descrizione: <descrizione dell'incantesimo>
libro: <libro>
usato_da: <personaggio>

Suggerisci un incantesimo per:
```{suggestion}```"""
    return base_prompt
