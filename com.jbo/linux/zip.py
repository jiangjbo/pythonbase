import zipfile

f = zipfile.ZipFile('temp.zip')
with open('passwords.txt') as pf:
    for line in pf:
        try:
            f.extractall(pwd=line.strip())
            print("password is {0}".format(line.strip()))
        except:
            pass
