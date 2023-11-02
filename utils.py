import threading
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
        exit(1)