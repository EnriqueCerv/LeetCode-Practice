# %%
def funWithAnagrams(text):
    # Write your code here
    wordSets = set()
    text = [str(word) for word in text]
    n = len(text)
    print(text, n)
    for ele in text:
        wordList = [char for char in ele]
        wordList.sort()
        wordSorted = ''.join(wordList)
        
        if wordSorted not in wordSets:
            wordSets.add(wordSorted)
        print(wordSets)
    # for i in range(n):
    #     print(i, text[i])
    #     wordList = [char for char in text[i]]
    #     print(wordList)
    #     wordList.sort()
    #     wordSorted = ''.join(wordList)
        
    #     if wordSorted not in wordSets:
    #         wordSets.add(wordSorted)
    #     else: 
    #         text.pop(i)

text = ["code","aaagmnrs","anagrams","doce"] 
# text = [str(word) for word in text]
funWithAnagrams(text)