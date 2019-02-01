import zipfile
#crack zip file with dictionary attack
def ex7():
    try:
        #first you have to define the directory of the zip file you want to enter, or if you know only the name of 
           #zip file you can just check the directories and search for the zip file you want
            #with the command os.listdir(path), which returns in a list all the names (files) of a directory you can check for 
            #your file
        myzip = zipfile.ZipFile('test_zip.zip')
           #raise exceptions
    except zipfile.BadZipfile:
        print("ERROR")
        quit()

        #start with no passowrd
    password = None
    #supposing that you have already a deictionary you just read every line of it (every line represents a candidate password)
    with open('english.txt','r') as f:
        passes = f.readlines()
        #iterate the list
        for x in passes:
            password = x.split('\n')[0]
            try:
                print(password)
                #encode the password to utf 8, which means that you encode that password to one 8 bit number
                pas = str.encode((password))
                #try your password
                myzip.extractall(pwd=pas)
                #print it
                print('Password cracked with : ',password)
                quit()
            except Exception:
                pass
        print('Password not found')
















































