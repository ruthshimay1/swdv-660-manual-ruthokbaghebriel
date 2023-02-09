def getInputPhrase():
    return input("Enter your phrase: ").lower()

def title():
    return print("This program will count the number of vowels in an input phrase.")

def getVowelCount(phrase):              
    vowelCount = 0
    for char in phrase:
        if char in ['a', 'i','e','o', 'u']:
            vowelCount +=1
    return vowelCount
    
# def printAnswer():
#     return print('Total vowels in your Phrase:  {}'.format(getVowelCount()))
    

def main():
    title()   
    inputPhrase = getInputPhrase()
    totalVowels = getVowelCount(inputPhrase)
    print('Total vowels in your Phrase:  {}'.format(totalVowels))
    
  

# _____________________________Run Code below result_______________
