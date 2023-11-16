import subprocess
import sys
from typing import Tuple
import os
from utils import path_exists, create_dir

'''
This file communicates with the OS to execute users' instructions.
It is responsible for running Python code and Unix commands.
'''


def run_command(command: str, working_dir: str = 'temp') -> Tuple[str, str]:
    '''
    Run command and return stdout and stderr
    '''
    # create temp directory if not exists
    if not path_exists(working_dir):
        create_dir(working_dir)

    current_dir = os.getcwd()
    try:
        os.chdir(working_dir)
        proc = subprocess.run(
            command.split(' '),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            timeout=5
        )
        return proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return '', 'Timeout expired'
    except Exception as e:
        return '', str(e)
    finally:
        os.chdir(current_dir)


def run_python_code(path: str) -> Tuple[str, str]:
    '''
    Run python code and return stdout and stderr
    '''
    try:
        current_dir = os.getcwd()
        os.chdir(os.path.dirname(path))
        proc = subprocess.run(
            ['python3', os.path.basename(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            timeout=5
        )
        os.chdir(current_dir)
        return proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return '', 'Timeout expired'
    except Exception as e:
        return '', str(e)


def run_node_code(path: str) -> Tuple[str, str]:
    '''
    Run node code and return stdout and stderr
    '''
    try:
        current_dir = os.getcwd()
        os.chdir(os.path.dirname(path))
        proc = subprocess.run(
            ['node', os.path.basename(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            timeout=5
        )
        os.chdir(current_dir)
        return proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return '', 'Timeout expired'
    except Exception as e:
        return '', str(e)


def get_cli() -> str:
    '''
    Get CLI arguments
    Sample usage: python3 code_runner.py <path_to_file>
    '''

    try:
        if len(sys.argv) != 2:
            raise Exception('Invalid number of arguments')

        return sys.argv[1]

    except Exception as e:
        print(str(e))
        exit(1)
