def encrypt(n):
    nList = []
    for x in range(len(n)):
        #Key: gets the unicode value, doubles it, then times
        #it by the index it's at, but adds 1, if not, first
        #index of every encrypted string would be the unicode
        #value of 0 (Anything multiplied by 0 is simply 0)
        nList.append(chr((ord(n[x]) * 2) * (x + 1)))

    for z in range(len(nList)):
        #Formats the list into a simple string
        nE = ''.join([str(c) for c in nList])
    return nE

def decrypt(n):
    nList = []
    
    for x in range(len(n)):
        #Essientally just the reverse of the Key
        nList.append(chr((ord(n[x]) // 2) // (x + 1)))


    for z in range(len(nList)):
        #Formats the list into a simple string
        nE = ''.join([str(c) for c in nList])
        print(nE)
    return nE   

    
while True:
    #One problem which can be common is when dealing with longer
    #strings the program will return an error as the value given
    #by the key will exceed the 144 thousand unicode characters
    #and hence return an error
    n = encrypt(input())
    print(n)
    print(decrypt(n))

    






