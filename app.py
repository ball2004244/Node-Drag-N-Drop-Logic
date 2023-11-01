from fastapi import FastAPI
from pydantic import BaseModel
from code_runner import create_file, run_python_code

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def running_code(code_req: CodeRequest):
    # get code from request
    code = code_req.code
    path = 'temp/code.py'
    
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