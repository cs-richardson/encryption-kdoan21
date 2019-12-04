#caesar
cipherText = ""
userText = input("What is your phrase? ")
shift = int(input("What is your shift? ")

for i in userText:
    if i.isalpha():
        stayInAlphabet = ord(i) + shift
            if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
print(cipherText)
