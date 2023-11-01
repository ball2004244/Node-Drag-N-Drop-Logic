# Python DragNDrop Backend
This is the server logic for the DragNDrop project. It is written in Python with FastAPI.

## Overview
This project enables user to code Python only using drag and drop. It is a web application that allows users to drag and drop blocks of code to create a Python program.

## Logic
The server have 3 modules:
- app.py: The main module that contains the FastAPI routers.
- code_runner.py: The module uses subprocess to run the code and return the output.
- code_translator.py: The module that translates the retrieved pseudo code to Python code.