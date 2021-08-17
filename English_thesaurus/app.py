import json
from difflib import get_close_matches

def getUserWord():
    word = input("Enter word: ")
    return word.strip().lower()

def getDict():
    dictKey = None
    try:
        dataFile = open('data.json', 'r')
        dictKey = json.load(dataFile)
    except Exception as e:
        print('getDict exception: ', e)
    
    return dictKey

def getUserConfirmContinueApp():
    while True:
        confirm = input("Do you want to continue app? [Y/N]: ").strip().upper()
        if confirm == 'Y':
            return True
        elif confirm == 'N':
            return False
        else:
            print('Incorrect selection!')

def getCloserWordsList(word, listWords):
    return get_close_matches(word, listWords, n=10)

def printListCloserWords(listWords):
    print("Word doesn't exist. List closer words: ")
    print("\n".join(listWords))

if __name__ == "__main__":
    remainApp = True

    while remainApp:
        word = getUserWord()
        dictKey = getDict()

        if word in dictKey:
            print(dictKey[word][0])
        else:
            closerList = getCloserWordsList(word, dictKey)
            if len(closerList) > 0:
                printListCloserWords(closerList)
            else:
                print("Word doesn't exist! Please check it again!")
        
        remainApp = getUserConfirmContinueApp()
