from decorator_output import beautify_output


@beautify_output
def today_quote():
    print("It's a beautiful sunny day")


today_quote()
