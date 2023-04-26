from gpt_client.client import GptClient as Client
from gpt_client.code_client import GptCodeClient as CodeClient

from gpt_client.cli_client_factory import cli_client_factory


import argparse



def generate_output_file(file_name: str):
    with open(f"output/{file_name}", "w") as file1:
    # Writing data to a file
        file1.write("")
        

def append_entry(file_name: str, role: str, entry: str):
    with open(f"output/{file_name}", "a") as file1:
    # Writing data to a file
        file1.write(f">> {role}:\n")
        file1.write("\n\n")
        file1.write(f"{entry}:\n")
        file1.write("\n\n")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate code from a prompt')
    parser.add_argument('--model', dest='model', type=str, default='gpt-3.5-turbo',
                        help='the model to use')

    parser.add_argument('--output', dest='output', type=str, default='',
                        help='the output file to use')
    parser.add_argument('--type', dest='assistant_type', type=str, default='normal',
                        choices=['normal', 'code'],
                        help='the type of assistant that should be used')
    
    args = parser.parse_args()

    assistant_type = args.assistant_type

    client = cli_client_factory(args.model, assistant_type, args.output)


    while True:
        client.run_interaction()
