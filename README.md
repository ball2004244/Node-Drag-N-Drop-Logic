# PyJSON Compiler

Allow user to code Python using Json syntax.

## Overview

This project allows users to code Python using Json syntax. It is a web server that receive, compile, and run pyJson code. The server is built using FastAPI and the code is compiled and run using Python subprocess module.

## Installation

You can install this project with 2 methods:

1. Clone this repository and run the server locally.
2. Install using Docker.

### 1. Direct Install

1. Clone this repository
2. Install the dependencies

```
pip install -r requirements.txt
```

3. Run the server at port 8000

```
uvicorn app:app --port 8000
```

### 2. Using Docker

1. Ensure that Docker is installed on your machine.
2. Pull the image from Docker Hub

```
docker pull ball2004244/pyjson-compiler
```

3. Run the image

```
docker run -d -p 8000:8000 ball2004244/pyjson-compiler
```

## Usage

Send a POST request to the server with the following body:

```
{
    "code": {
        "print": "'Hello World!'",
        "print2": "'I am PyJSON'"
    },
    "filename": "code.py"
}
```

Output:

```
Hello World!
I am PyJSON
```

## Supported Keywords

| Keyword | Description               | Example              |
| ------- | ------------------------- | -------------------- |
| print   | Print a string to console | print('Hello World') |

This part is under construction!

See [Config](pyjson.config.json) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Upcoming Features

- File Read/Write Support
- Variable/Constant
- Maths Operation
- Data Type
