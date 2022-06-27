# compress return the only those items for which the corresponding selector value is true
from itertools import compress

traveller = ["Priti", "Vimmi", "Timmi"]
have_symptoms = [False, True, True]

traveller_have_symptoms = compress(traveller, have_symptoms)
print(list(traveller_have_symptoms))
