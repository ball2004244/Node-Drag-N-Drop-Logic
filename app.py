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

@app.post("/")
async def running_code(code_req: CodeRequest):
    # get code from request
    json_code = code_req.code
    path = 'temp/code.py'
    
    translator = Translator(json_code)
    code = translator.convert()

    # create file
    create_file(path, code)
    
    # run code
    output = run_python_code(path)
    
    response = {
        'status': 'success',
        'stdout': output[0],
        'stderr': output[1]
    }
    
    return response