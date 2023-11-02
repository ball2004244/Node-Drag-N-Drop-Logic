import threading
from typing import Callable

def run_thread(func: Callable, *args, **kwargs) -> None:
    # create thread
    t = threading.Thread(target=func, args=args, kwargs=kwargs)
    
    # run thread
    t.start()

    # end thread
    t.join()
