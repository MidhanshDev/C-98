def countwordsfromfile():
    fileName = input (" Enter the file name ")
    numberofwords = 0
    file = open(fileName,"r")
    for line in file:
        words = line.split()
        numberofwords=numberofwords+len(words)
    print("Number of words present in the file = ",numberofwords)


countwordsfromfile()
