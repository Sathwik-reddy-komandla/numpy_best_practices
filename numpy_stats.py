import numpy as np
func_names=[
    "mean",
    "median",
    "var",
    "std",
    "min",
    "max",
]
def calculate(numbers:iter):
    funcs=[getattr(np,func) for func in func_names]
    result={}
    for name,func in zip(func_names,funcs):
        result[name]=func(numbers)
    return result


def execute():
    funcs=calculate(range(1,201))
    return funcs


if __name__=="__main__":
    funcs=execute()
    print(funcs)
  