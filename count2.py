#counts and returns the number of words in a given text.

#creating a function
def count_words():
    f = open("textfile.txt", "r")
    lines=f.read()
    words=lines.split()
    print("\nThe total number of words in the textfile is:",len(words))
    f.close()

count_words()