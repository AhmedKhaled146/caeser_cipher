def caeser_cipher():
    text = input("enter the text\n")
    k = int(input("enter the k\n"))
    result = ""
    for i in range(len(text)):
        char = text[i]
        if text[i] == ' ':
            L = ' '
        elif char.isupper():
            L = chr((ord(char)-65+k) %26+65 )
        else:
            L = chr((ord(char)-97+k) %26+97)

            
        result+=L
    print(result)
    
caeser_cipher()