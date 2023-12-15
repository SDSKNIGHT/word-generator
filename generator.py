import sys
import nltk
from nltk.corpus import words
import random


def generator(length):
    output=[]
    # thiswords = words.words()

    words10000=open("google-10000-english.txt", "r") 
    data = words10000.read() 
    
 
    thiswords = data.split("\n") 

    for i in range(length*100):
        output+=[thiswords[random.randint(0,len(thiswords))]]
        
    return output

# code that generates a random assortment of words of a given length







    


if __name__ == "__main__":
    nltk.download('words')
    script = generator(int(sys.argv[1]))


    
    with open('hallucination inducer.txt', 'w') as file:
        # Write some content to the file
        file.write(" ".join(script))