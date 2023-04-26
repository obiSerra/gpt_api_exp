from gpt_client.client import GptClient



class GptCodeClient(GptClient):

    def __init__(self, model: str = "gpt-3.5-turbo"):
        super().__init__(model)

        starting_prompt = "You are a code generation AI, your responses will only contain code. Any comment, note or explanation will be inserted inside a comment. Answer 'Yes' if you understand and after that do not generate anything that is not valid code."

        self.message_history = [{"role": "user", "content": starting_prompt}, {"role": "assistant", "content": "Yes"}]