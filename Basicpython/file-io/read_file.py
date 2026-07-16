def readfile():
    file = open("C:/Users/udayd/OneDrive/Desktop/abc.txt", 'r')
    text = file.read()
    print(text)
    file.close()


readfile()
