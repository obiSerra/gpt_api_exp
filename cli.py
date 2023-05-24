import argparse
import json

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

    args = parser.parse_args()
    with open(args.input_file, "r") as f:
        prompt = f.read()

    client = GptClient(model=args.model)

    full_prompt = f""" Your job is to perform the following tasks; for each task generate a separtate section:
1. Read the text delimited by triple underscore (___).
2. Write a summary of it, highlighting the most important concepts.
3. Rephrase the summary as it was a paragraph from a blog post.


___
{prompt}
___
"""
    for _ in range(1):
        client.answer(full_prompt)
        # print(full_prompt)
        answer = client.last_answer()
        # print(answer)
        with open(f"output/{args.output}.txt", "w") as f:
            f.write("Prompt:\n\n")
            f.write(full_prompt)
            f.write("\n\nCompletion:\n\n")
            f.write(answer)
    print("Done!")
