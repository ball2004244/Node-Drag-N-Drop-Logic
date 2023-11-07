import subprocess
import sys
from typing import Tuple
import os

def run_command(command: str, working_dir: str = 'temp') -> Tuple[str, str]:
    '''
    Run command and return stdout and stderr
    '''
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


def main():
    '''
    Main function
    '''
    try:
        # get cli arguments
        path = get_cli()

        code = ''
        with open(path, 'r') as f:
            code = f.read()

        stdout, stderr = run_python_code(path)
        print('------------------')
        print('Original code:\n%s' % code)
        print('------------------')
        print('stdout:\n%s' % (stdout if stdout else None))
        print('stderr:\n%s' % (stderr if stderr else None))
        print('------------------')

    except Exception as e:
        print(None, str(e))


if __name__ == '__main__':
    main()
