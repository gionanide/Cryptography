import zipfile
#crack zip file with dictionary attack
def ex7():
    try:
        myzip = zipfile.ZipFile('test_zip.zip')
    except zipfile.BadZipfile:
        print("ERROR")
        quit()

    password = None
    with open('english.txt','r') as f:
        passes = f.readlines()
        for x in passes:
            password = x.split('\n')[0]
            try:
                print(password)
                pas = str.encode((password))
                myzip.extractall(pwd=pas)
                print('Password cracked with : ',password)
                quit()
            except Exception:
                pass
        print('Password not found')
















































