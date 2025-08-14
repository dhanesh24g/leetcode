s = "1A man, a plan, a canal: Panama1"

pal = ""

for i, val in enumerate(s):

    if val.isalnum():
        pal += val.lower()

print(pal==pal[::-1])