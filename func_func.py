import numpy as np

def func_to_func(f:callable)-> None:
    print(f.__name__)
    print(f.__module__)
    print(f(range(1,11)))


if __name__=="__main__":
    func_to_func(np.sum)