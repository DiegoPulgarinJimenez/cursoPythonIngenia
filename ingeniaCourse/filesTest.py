from io import open

"""textFile1 = open('file1.txt', 'w')
string1 = "the roses are red \nthe sky is blue"
textFile1.write(string1)
textFile1.close()"""
textFile1 = open('file1.txt', 'r+')  # r+ for reading and writing simultaneously
addNumber = 12
textFile1.writelines(str(addNumber))
readingData = textFile1.read()
textFile1.close()
print(readingData)
