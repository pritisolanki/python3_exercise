from email.quoprimime import quote
from decorator_output import beautify_output
from decorator_output import beautify_output_withlen


@beautify_output
def today_quote():
    print("It's a beautiful sunny day")


@beautify_output_withlen
def today_motivation(q):
    print(q)


q = "One day!"
today_motivation(q)
