from pydantic import BaseModel
from typing import Dict

class CodeRequest(BaseModel):
    filename: str
    code: Dict[str, str]

class CLIRequest(BaseModel):
    command: str