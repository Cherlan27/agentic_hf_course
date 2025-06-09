from pydantic import BaseModel

class PromptData(BaseModel):
    prompt: str
    max_new_tokens: int