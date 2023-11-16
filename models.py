from pydantic import BaseModel
from typing import Dict, Union, List

'''
This file define the request and response body for the API.
'''


class CodeRequest(BaseModel):
    filename: str
    code: Dict[str, Union[str, List[str]]]


class CLIRequest(BaseModel):
    command: str
