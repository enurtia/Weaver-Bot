import numpy as np

class wordObj:
    def __init__(self, word):
        self.word = word
        self.neighbors = []

    def setNeighbors(self, wordList):
        for w in wordList:
            difCount = 0
            for i in range(4):
                if(w[i] != self.word[i]):
                    difCount += 1
            if difCount == 1:
                self.neighbors += [w]

def getShortestPath(wordsList, startingWord, endingWord):
    allWords = wordsList.copy()
    unvisited = wordsList.copy()
    wordMap = {}
    distance = {}
    lastNode = {}
    
    for wordObj in allWords:
        distance[wordObj] = float('inf')
        lastNode[wordObj] = None
        wordMap[wordObj.word] = wordObj
    
    startingWordObj = wordMap[startingWord]
    nodeQueue = np.delete(allWords, np.where(allWords == startingWordObj))
    distance[wordMap[startingWord]] = 0
    
    def getMinDist(distancesList):
        least = float('inf')
        leastKey = None
        for key in distancesList:
            #print(key.word, " ", distance[key]) 
            if distance[key] < least:
                least = distance[key]
                leastKey = key
                
        return leastKey
    
    while unvisited.size != 0:
        curNode = getMinDist(unvisited)
        
        if curNode is None:
            break
        
        for neighbor in curNode.neighbors:
            neighborObj = wordMap[neighbor]
            if neighborObj in unvisited:
                tempDist = distance[curNode] + 1
                if tempDist < distance[neighborObj]:
                    distance[neighborObj] = tempDist
                    lastNode[neighborObj] = curNode
                    
        unvisited = np.delete(unvisited, np.where(unvisited == curNode))
        
        
    curWordObj = wordMap[endingWord]
    path = [curWordObj.word]
    while (lastNode[curWordObj] is not startingWordObj) and lastNode[curWordObj] is not None:
        nextWordObj = lastNode[curWordObj]
        path += [nextWordObj.word]
        curWordObj = nextWordObj
    path += [startingWordObj.word]
    
    if path[-1] is None:
        print("No valid path found in word list.")
    else:
        print(path[::-1])
    

#---------Load 4 letter words---------
words = np.loadtxt("PATH.txt", dtype=str)
words = np.char.lower(words)
    
startWord = input("Start word: ").lower()
endWord = input("End Word: ").lower()
    
while True:
    wordObjects = np.empty(0)
    for word in words:
        w = wordObj(word)
        w.setNeighbors(words)
        wordObjects = np.append(wordObjects, w)

    getShortestPath(wordObjects, startWord, endWord)
    removeWordRaw = input("Remove word/words (comma separate), or just press enter: ").lower()
    removeWordArr = removeWordRaw.replace(" ", "").split(",")
    
    if len(removeWordRaw) == 0:
        break
    
    for removalWord in removeWordArr:
        if removalWord != startWord and removalWord != endWord:
            words = np.delete(words, np.where(words == removalWord))
