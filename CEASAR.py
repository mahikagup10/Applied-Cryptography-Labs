key = 10
pt = "CRYPTOGRAPHY"
print("Plaintext:",pt)
ct = ""
dt = ""

for i in range(len(pt)):
    char = pt[i]
    if char.isupper():
        if (ord(char)+key-1)>90:
            ct += chr(65+90-ord(char))
        else:
            ct += chr(ord(char)+key)
    else: 
        if (ord(char)+key-1)>122:
            ct += chr(97+122-ord(char))
        else:
            ct += chr(ord(char)+key)


for i in range(len(ct)):
    chard = ct[i]
    if chard.isupper():
        # if (ord(c)-65)>25:
        #ct = chr(ord(c)+key)
        if (ord(chard)-key+1)<65:
            dt += chr(65+90-ord(chard))
        else:
            dt += chr(ord(chard)-key)
    else: 
        if (ord(chard)-key+1)<97:
            dt += chr(97+122-ord(chard))
        else:
            dt += chr(ord(chard)-key)


    

print("cipher text:",ct)

print("Deciphered text:",dt)




