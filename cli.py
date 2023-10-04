import argparse

from jinja2 import Environment, FileSystemLoader


from gpt_client.client import GptClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate code from a prompt")

    parser.add_argument(
        "--model",
        dest="model",
        type=str,
        default="gpt-3.5-turbo",
        help="the model to use",
    )

    parser.add_argument(dest="input_file", type=str, help="the input file to for the prompt")
    parser.add_argument("--output", dest="output", default="out", type=str, help="the output file to use")
    parser.add_argument("--meta", dest="meta", default="base", type=str, help="the meta-prompt to use")

    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        prompt = f.read()

    client = GptClient(model=args.model)

    environment = Environment(loader=FileSystemLoader("metaprompt_templates/"))
    template = environment.get_template(f"{args.meta}.jinja2")

    style = " from a technical wiki"

    full_prompt = template.render(prompt=prompt)

    for _ in range(1):
        client.answer(full_prompt)
        # print(full_prompt)
        answer = client.last_answer()
        print(answer)
        with open(f"output/{args.output}.txt", "w") as f:
            f.write("Prompt:\n\n")
            f.write(full_prompt)
            f.write("\n\nCompletion:\n\n")
            f.write(answer)
    print("\n\none!")
