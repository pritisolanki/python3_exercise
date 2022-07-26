import time


def beautify_output(func):
    def wrapper_output():
        print("-----------------------------")
        func()
        print("-----------------------------")

    return wrapper_output


def beautify_output_withlen(func):
    def wrapper_output(*args, **kwargs):
        print("-" * len(args[0]))
        func(*args, **kwargs)
        print("-" * len(args[0]))

    return wrapper_output


def addtimer(func):
    def wrapper_addtimer(*args, **kwargs):
        tic = time.perf_counter()
        func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"Function {func.__name__}() took  {toc - tic:0.4f} seconds")

    return wrapper_addtimer
