import random as rd
from string import digits as dig
from string import punctuation as pun
from string import ascii_letters as asc

symbols = asc + dig + pun
secure_random = rd.SystemRandom()
password = "".join(secure_random.choice(symbols)
                   for i in range(20))
print(password)
