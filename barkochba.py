import sys
import random

titok = random.randint(1, 100)
print("Gondoltam egy számra 1 és 100 között")

kör = 0

for line in sys.stdin:
    kör = kör + 1
    input = line.rstrip()
    if 'Exit' == input:
        break

    try:
        tipp = int(input)
    except:
        print("A(z)", input, "nem egy szám")
        continue

    if tipp < titok:
        print("Egy nagyobb számra gondoltam")

    if tipp > titok:
        print("Egy kissebb számra gondoltam")

    if tipp == titok:
        print("Gratulálok kitaláltad a számot")
        print(kör, "tippből sikerült rájönnöd")
        break

print("Done")
