from requests import Response
import requests

from agentic_hf_course.data_structure import PromptData



class ApiHandler():
    def __init__(self, url: str):
        self.url = url

    def generate(self, data: PromptData) -> Response:
        """
        Send prompt data to LLM model and get response

        Args:
            data (PromptData): Prompt with max tokens
        
        Returns:

        """
        try:
            response = requests.post(
                url = self.url,
                json = data
            )
            return response
        except:
            print("Error with API")

