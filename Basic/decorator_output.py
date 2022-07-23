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
