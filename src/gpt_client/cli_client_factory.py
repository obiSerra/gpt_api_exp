from gpt_client.client import GptClient as Client
from gpt_client.code_client import GptCodeClient as CodeClient



import argparse


class CliClient:
    prompt = "[+] Your input: "
    response_indicator = "[>] AI response: "

    def __init__(self, client: Client, file_name: str):
        self.client = client
        self.file_name = file_name

        if file_name:
            self.generate_output_file()

    def _log_append_interaction(self, prompt: str, response: str):
        self.append_entry("user", prompt)
        self.append_entry("assistant", response)

    def _on_interaction_end(self):
        pass

    def run_interaction(self):
        prompt = input(self.prompt)
        self.client.user_prompt(prompt)
        self.client.completion()
        print(self.response_indicator)
        print("")
        response = self.client.assistant_response()
        if self.file_name:
            self._log_append_interaction(prompt, response)
        
        print(response)
        print("")
        self._on_interaction_end()

    def generate_output_file(self):
        with open(f"output/{self.file_name}", "w") as file1:
        # Writing data to a file
            file1.write("")

    def append_entry(self, role: str, entry: str):
        with open(f"output/{self.file_name}", "a") as file1:
        # Writing data to a file
            file1.write(f">> {role}:\n")
            file1.write("\n\n")
            file1.write(f"{entry}:\n")
            file1.write("\n\n")


class CliCodeClient(CliClient):

    prompt = "[+] (Generate the code for): "
    
    def append_entry(self, role: str, entry: str):
        e = entry.replace("```", "")
        with open(f"output/{self.file_name}", "a") as file1:
            file1.write(f"\n{e}\n")
    
    def _log_append_interaction(self, _: str, response: str):
        self.append_entry("assistant", response)

    def _on_interaction_end(self):
        exit()



def cli_client_factory(model:str, assistant_type:str, output:str):
    if assistant_type == "normal":
        return CliClient(Client(model), output)
    elif assistant_type == "code":
        return CliCodeClient(CodeClient(model), output)
    else:
        raise ValueError("Unknown role")



        





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
    if assistant_type == "normal":
        gpt_client = Client(args.model)
    elif assistant_type == "code":
        gpt_client = CodeClient(args.model)
    print(f"Using: {assistant_type}")

    print(gpt_client.message_history)

    if args.output:
        generate_output_file(args.output)

    while True:
        prompt = input("[+] Your input: ")
        gpt_client.user_prompt(prompt)
        gpt_client.completion()
        print("[>] AI response: ")
        print("")
        response = gpt_client.assistant_response()
        if args.output:
            append_entry(args.output, "user", prompt)
            append_entry(args.output, "assistant", response)
        print(response)
        print("")
