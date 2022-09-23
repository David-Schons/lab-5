encodedWord = "UUHO"
recognizeU = False
decodedWord = ""
for letter in encodedWord:
    if letter == "L":
        decodedWord = decodedWord+("T")
    elif letter == "T":
        decodedWord = decodedWord+("L")
    elif letter == "8":
        decodedWord = decodedWord+("A")
    elif letter == "B":
        decodedWord = decodedWord+("A")
    elif letter == "A":
        decodedWord = decodedWord+("E")
    elif letter == "E":
        decodedWord = decodedWord+("B")
    elif letter == "U":
        if recognizeU == True:
            decodedWord = decodedWord+ ("")
        elif recognizeU == False:
            decodedWord = decodedWord + ("W")
            recognizeU = True
    else:
        decodedWord = decodedWord+(letter)

print(decodedWord)

