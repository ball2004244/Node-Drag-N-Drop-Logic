import subprocess
import sys
from typing import Tuple

def create_file(path: str, content: str) -> None:
    '''
    Create file at path with content
    '''
    try:
        with open(path, 'w') as f:
            f.write(content)
    except Exception as e:
        print(str(e))
        exit(1)

def run_code(path: str) -> Tuple[str, str]:
    '''
    Run node code and return stdout and stderr
    '''
    try:
        proc = subprocess.run(
            ['node', path],
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

        stdout, stderr = run_code(code)
        print(stdout, stderr)

    except Exception as e:
        print(None, str(e))


if __name__ == '__main__':
    # main()
    path = input('Enter path: ')
    code = ''
    with open(path, 'r') as f:
        code = f.read()
        
    stdout, stderr = run_code(code)
    print(stdout, stderr)
