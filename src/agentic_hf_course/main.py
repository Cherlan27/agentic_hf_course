from agentic_hf_course.api import ApiHandler
from agentic_hf_course.data_structure import PromptData


def main_loop(url: str):
    """
    Main loop framework to ask LLM questions

    Args:
        url (str): Url for reaching out to model
    """
    token_number = int(input("Set max number tokens (int):"))
    input_str = ""
    
    while input_str != "exit":
        input_str = input("Write your prompt")
        llm = ApiHandler(url)

        response = llm.generate(
            PromptData(
                prompt = input_str, 
                max_new_tokens=token_number
            )
        )

        print(response)
        print("\n")


if __name__ == "__main__":
    main_loop(url = "http://localhost:8000/generate")