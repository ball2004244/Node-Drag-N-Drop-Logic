from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from code_runner import run_python_code
from code_translator import Translator
from typing import Dict
from utils import create_file

app = FastAPI()

# Allow CORS from all origins, only allow GET, PUT, POST, and DELETE methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "PUT", "POST", "DELETE"],
)


class CodeRequest(BaseModel):
    code: Dict[str, str]


@app.get("/")
async def root():
    return {"message": "Hello World"}

RESPONSE_TEMPLATE = {
    'status': 'success',
    'stdout': '',
    'stderr': ''
}


@app.post("/")
async def running_code(code_req: CodeRequest):
    # get code from request
    json_code = code_req.code
    path = 'temp/code.py'

    translator = Translator(json_code)
    code = translator.convert()

    response = RESPONSE_TEMPLATE.copy()

    if code[0] == 'error':
        response['status'] = 'error'
        response['stderr'] = code[1]
        return response

    # create file
    create_file(path, code[1])

    # run code
    output = run_python_code(path)

    if output[1]:
        response['status'] = 'error'
        response['stderr'] = output[1]
        return response

    response['stdout'] = output[0]
    return response
