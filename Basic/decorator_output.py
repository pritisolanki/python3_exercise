def beautify_output(func):
    def wrapper_output():
        print("-----------------------------")
        func()
        print("-----------------------------")

    return wrapper_output
