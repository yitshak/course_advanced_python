
import os
from contextlib import contextmanager
import time


##1
@contextmanager
def cd(where):
    current_dir = os.getcwd()
    os.chdir(where)
    try:
        yield
    finally:
        os.chdir(current_dir)



print(os.getcwd())
with cd("\\"):
    print(os.getcwd())

print(os.getcwd())


##2
@contextmanager
def timeme():
    current_time = time.time()
    try:
        yield
    finally:
        execution_time = time.time() - current_time
        print("--- The opration took {:0.4} ms".format(execution_time*1000))



with timeme():
    j=0
    for i in range(100000):
        j+=1

