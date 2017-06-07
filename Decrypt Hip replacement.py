
import timeit


def ex4():
    text = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    textL = list(text)

    #Brude Force algorithm
    print('Message is: ',text)

    size = len(text)
    for i in range(1,26):
        for k in range(size):
            letterNumber = ord(textL[k])
            nextNumber = letterNumber + 1
            if(nextNumber > 90):
                nextNumber = nextNumber - 90 + 64
            textL[k] = chr(nextNumber)
        print(i,'Decrypting message: ',"".join(textL))

        if((distance1%k==0) and (distance2%k==0)):
