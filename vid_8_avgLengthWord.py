# B_R_R
# M_S_A_W

"""
Task is, we have to find avarage word length for each line.
"""
with open('test.txt','w')as wf:
    wf.write("Some new line code goes here,\nI forgot to start with the name of GOD,\nthen sending salutation upon"
             "our beloved prophet,\nI want to be professional and expert programmer,\nEspecially of Python")

with open('test.txt', 'r')as rf:
    lineNum=1
    while True:
        line=rf.readline()

        if not line:
            break

        print("Line: ",lineNum)

        wordList=line.split() #splits the sentence into words

        print("Number of words: ", len(wordList)) # then counts words and prints out

        #how many characters in our list
        our_char=0
        for word in wordList:
            for char in word:
                our_char+=1

        # average character in our line of words
        avg_char=our_char/len(wordList)
        print("Average word length: {:.2}\n".format(avg_char))

        lineNum+=1
