#RC4 algorithm with 5-bit encryption
aDict = dict(zip('abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                              ['00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001',
                              '11010','11011','11100','11101','11110','11111',
                              '00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001'])) #the function from our alphabet to 5-bit binary strings


#xor logical gate python
#this my implementation of XOR gate
def sxor(s1, s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    s1 = '{0:010b}'.format(s1)
    s2 = '{0:010b}'.format(s2)
    number = [0]*len(s1)
    for x in range(len(s1)):
        if(s1[x]==s2[x]):
            number[x] = 0
        elif(not(s1[x]==s2[x])):
            number[x] = 1
    #number1 = ''.join(map(str, number))
    number1 = (''.join(map(str, number)))
    number = int(number1, 2)
    return number



# the function below converts a text of the form 'something' to
# a binary string according to our 5-bit encoding
def text_enc(text):
    text = text[::-1]
    length = len(text)
    coded_text = ''
    for i in range(length):
        coded_text = aDict[text[i]]+ coded_text
    return coded_text.lower()

# The function below converts a binary string to an alphabetic text
# according to our 5-bit encoding
def text_dec(binary_string):
    length = len(binary_string)
    inv_map = {v: k for k, v in aDict.items()}
    decoded_text = ''
    for i in range(0, length, 5):
        decoded_text = inv_map[binary_string[i:i + 5]] + decoded_text  # + in strings is the join function.
    decoded_text = decoded_text[::-1]
    return decoded_text.lower()


def ex2():
    a='WE ALL MAKE MISTAKES AND WE ALL PAY A PRICE'
    key='HOUSE'
    #make the text without gaps
    text=a.replace(" ", "")
    print('Text: ',text)
    print('Key; ',key)
    keyByte = text_enc(key)
    textByte = text_enc(text)


    keystreamList = []
    cipherList = []
    keyLength = len(keyByte)
    print('Key in five-bit encoding: ',keyByte)
    textLength = len(textByte)
    print('Message in five-bit encoding: ',textByte)
    S=[0]*256
    for x in range(256):
        S[x] = x

    keyBytes = [0]*keyLength
    for x in range(keyLength):
        if(ord(keyByte[x])==48):
            keyBytes[x] = 0
        else:
            keyBytes[x] = 1



    j = 0
    for i in range(256):
        j = (j + S[i] + keyBytes[i % keyLength]) % 256
        S[i], S[j] = S[j], S[i]

    textBytes = [0]*textLength
    for x in range(textLength):
        if(ord(textByte[x])==48):
            textBytes[x] = 0
        else:
            textBytes[x] = 1

    i = 0
    j = 0
    out = []
    for m in range(textLength):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        keystreamList.append(k)
        cipherList.append(pow(k,textBytes[m]))



    finalArray = [0]*len(cipherList)
    for x in range(len(cipherList)):
        finalArray[x] = sxor(cipherList[x],keystreamList[x])

    finalText = [" "]*textLength
    for x in range(textLength):
        finalText[x] = chr(finalArray[x])

    print('Final Encrypted text: ')
    print("".join(finalText))
















































