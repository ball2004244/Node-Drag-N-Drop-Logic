import threading
import os
from typing import Callable

def run_thread(func: Callable, *args, **kwargs) -> None:
    # create thread
    t = threading.Thread(target=func, args=args, kwargs=kwargs)
    
    # run thread
    t.start()

    # end thread
    t.join()

def create_file(path: str, content: str) -> None:
    '''
    Create file at path with content
    '''
    try:
        with open(path, 'w') as f:
            f.write(content)
    except Exception as e:
        print(str(e))

def path_exists(path: str) -> bool:
    '''
    Check if path exists
    '''
    try:
        return os.path.exists(path)
    except Exception as e:
        print(str(e))
        return False

def create_dir(path: str) -> None:
    '''
    Create directory at path
    '''
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(str(e))

def create_path(path: str, content: str, overwrite: bool = False) -> None:
    '''
    Check and create path
    '''
    current_dir = os.getcwd()

    try:
        if path_exists(path) and not overwrite:
            raise Exception('Path already exists')
        
        # the last element is the file name, the rest is the pre_path
        pre_path, filename = os.path.split(path)
        
        create_dir(pre_path)
        
        os.chdir(pre_path)
        create_file(filename, content)
        os.chdir('..')

    except Exception as e:
        print(str(e))
    finally:
        os.chdir(current_dir)
    
if __name__ == '__main__':
    create_path('tester/test2/nothin/test.txt', 'hello world', overwrite=True)