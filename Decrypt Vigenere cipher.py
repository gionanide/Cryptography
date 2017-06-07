#decryption  for vigenere cipher
def ex3():
    flag=1
    with open('vigenere.txt','r') as textFile:
        for line in textFile.readlines():
            text = line
    textLength = len(text)

    i=1
    #i am going to check the key's length , about 100 letters
    #sequence array
    print('Sequency array numbers for 100 replacements')
    sum=[]
    for i in range(100):
        sum.append(0)
        #first iteration
    for k in range(100):
        for x in range(textLength - i):
            if(x+i < textLength):
                if( text[x+i] == text[x] ):
                    sum[k] = sum[k] + 1
        print(sum[k])
        i = i + 1

    #initialize the position array
    max=sum[0]
    for k in range(1,100):
        if(sum[k]>max):
            max=sum[k]
            position=k
    print('Max element:',max,' ,and the position:',position)

    #find the biggest element in the array and chech the distance
    #one to the end and one to the beggining
    difference=100000000
    distance1=0
    for k in range(position+1,100):
        if(sum[position]-sum[k]<difference):
            difference = sum[position]-sum[k]
            distance1 = k - position
    print('Position of biggest element starting from the max position going to the end:',distance1)
    difference = 100000000
    distance2=0
    for k in range(0,position-1):
        if (sum[position] - sum[k] < difference):
            difference = sum[position] - sum[k]
            distance2 = position - k
    print('Position of biggest element starting from the start and ends to max elements position:', distance2)

    print('Now I am searching for their common divisors who are the candidate lengths for the encryption key:')
    div=[]
    #check the smallest distance in order to use it in the iteration of finding the distance divisors
    if(distance1-distance2>0):
        smallestDistance=distance2
    else:
        smallestDistance=distance1

    for k in range(2,smallestDistance):
        if((distance1%k==0) and (distance2%k==0)):
            div.append(k)
    for k in range(len(div)):
        print(div[k])

    print('Selecting the maximum length')
    max = div[0]
    for k in range(1, len(div)):
        if (div[k] > max):
            max = div[k]
    print('Max divisor:', max)
    vigenereDecrypt(max,text,flag)

#starting letter's frequency for every array in the list
def vigenereDecrypt(keyLength,text,flag):
    print(text,'\n')
    lists=[[] for x in range(keyLength)]
    for x in range(len(text)):
        lists[x%keyLength].append(text[x])

    # i make a variable fot rhe entering procedure. This variable marks the input position of the elements
    #for ecxample element in position 0
    eternalTextLength=len(text)
    i=0
    print('I am going to group the letters with the length of the key\n')
    for x in range(keyLength):
        print('List before decryption: ',"".join(lists[x]))
        countLettersFrequency(lists[x])
    listAAA = makeFinalText(lists, eternalTextLength, flag, keyLength)
    print('Message before Decryption: ',text)
    print('Size: ',len(text))
    print('Message after decryption: ',"".join(listAAA))
    print('Size: ',len(listAAA))



#count frequency of letters in every list that i make based on the key length
def countLettersFrequency(list):
    import collections
    #letters sorted by the their frequency in the english alqhabet
    frequencyArray=['E','T','A','O','I','N','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z']
    letters = collections.Counter(list)
    print(len(list))
    max=-1
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if(letters[letter]>max):
            max=letters[letter]
            maxLetter=letter
    print('I found the letter with the biggest frequency: ',maxLetter,' and I suppose that this letter is'
          ' the first letter of my frequencyArray: ',frequencyArray[0])
    difference2 =ord(frequencyArray[0]) - ord(maxLetter)
    #in order to make replacement with the right way,checking for negative numbers
    if(difference2<0):
        difference2 = abs(difference2)
    #because i do not want to go front i want to go backwards to the alphabet
    difference1 = 26 - difference2
    if(difference1<0):
        difference1 = abs(difference1)
    print('And they have been encrypted with hip replacement, this means that the difference between this letter is'
          ' the key.')
    print('The hip replacement system of this team uses the following key: ','"',difference1,'"','. And I am going to use it'
          ' in order to decrypt only this team of letters . For the following teams I continue this procedure')
    hipReplacementDecrypt(list,difference1)


#decrypt the hip replacement encyption
def hipReplacementDecrypt(list,difference1):
    for x in range(len(list)):
        #put elements into the final text
        #for example element in position comes. x=0 0*keyLength = 0 and goes to the first position.
        #next element x=1 goes to 1*11=11 to position mumber 11 and repeatly to the end
        letterNumber = ord(list[x])
        nextNumber = letterNumber + difference1
        if (nextNumber > 90):
            nextNumber = nextNumber - 90 + 64
        list[x] = chr(nextNumber)
    print('Decrypting hip replacement message: ', "".join(list))
    print('End of the team \n')
    #now i have to join all the arrays together
    #joining the arrays procedure begins

#making the final text
def makeFinalText(lists,eternalTextLength,flag,keyLength):
    if (flag == 1):
        decryptionList = [' '] * eternalTextLength
        flag = 2
        print('Final textList initialize correctly\n')
    listNumber=0
    elementNumber=0
    for x in range(eternalTextLength):
        if(not(x==0)):
            if(x%keyLength==0):
                listNumber = 0
                elementNumber = elementNumber + 1
        decryptionList[x] = lists[listNumber][elementNumber]
        listNumber = listNumber + 1
    return decryptionList







