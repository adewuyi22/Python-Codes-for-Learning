'''
subject = input("Type a Word: ")
anagram = input("Type an Anagram: ")

if(len(subject)==len(anagram)):
    sorted_str1=sorted(subject)
    sorted_str2=sorted(anagram)

    if(sorted_str1 == sorted_str2):
        #print(subject + " and " + anagram + " are anagram.") 
        print("\nTrue")
    else:
        print("\nFalse")
else:
    print(subject + " and "+ anagram + " are not anagram.")
'''

# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #return True

    if(len(word)==len(anagram)):
        sorted_str1=sorted(word)
        sorted_str2=sorted(anagram)

        if(sorted_str1 == sorted_str2):
            print("\nTrue")  
            #return True
        else:
            print("\nFalse")
            #return False
    else:
        print(word + " and "+ anagram + " are not anagram.")

find_anagram("eat", "ate") #The program will return True because they are anagrams.
