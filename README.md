# PyJSON Compiler

Allow user to code Python using Json syntax.

## Overview

This project enables user to code Python only using drag and drop. It is a web application that allows users to drag and drop blocks of code to create a Python program.

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
docker pull ball2004244/python-drag-drop
```

3. Run the image

```
docker run -d -p 8000:8000 ball2004244/python-drag-drop
```

## Usage

Send a POST request to the server with the following body:

```
{
    "code": "your code here"
}
```

## Example

### Input

```
{
    "code": "print('Hello World')"
}
```

### Output

```
Hello World
```

## Supported Keywords

| Keyword | Description               | Example              |
| ------- | ------------------------- | -------------------- |
| print   | Print a string to console | print('Hello World') |

This part is under construction!

See [Config](pyjson.cofig.json) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Upcoming Features

- File Read/Write Support
- Variable/Constant
- Maths Operation
- Data Type
