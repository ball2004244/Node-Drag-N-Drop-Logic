import sys
sys.path.append('..')
from code_runner import run_command

def test_run_command():
    command = input('Enter command: ')
    
    stdout, stderr = run_command(command)
    status = 'Success' if stderr == '' else 'Error'
    
    print(f'\nRun status: {status}\n')
    print(f'Stdout: {stdout}\n')
    print(f'Stderr: {stderr}\n')
    
if __name__ == '__main__':
    test_run_command()