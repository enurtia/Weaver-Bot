import numpy as np 


#Letter our 4-letter wordlist
words = np.loadtxt("4LetterWords.txt", dtype=str)
words = np.char.lower(words)

startWord = input("Start word: ").lower()
endWord = input("End Word: ").lower()


#Pre-process words with HashMap before creating adjacency list.

hashMap = {}
for word in words:
	#abcd: 1bcd, a2cd, ab3d, abc4
	for j in range(len(word)):
		key = word[:j] + str(j+1) + word[j+1:]
		if key not in hashMap:
			hashMap[key] = [word]
		else:
			hashMap[key] += [word]


#Create adjacency list
dist = {}
adjacencyList = {}
for word in words:
	dist[word] = float("inf")
	adjacencyList[word] = []
	for j in range(len(word)):
		key = word[:j] + str(j+1) + word[j+1:]
		adjacencyList[word] += hashMap[key] #Will contain 4 instances of our word


#Breadth-First Search
dist[startWord] = 0
queue = [startWord]
pathTraversal = {}

while(len(queue)) != 0:
	u = queue.pop(0)
	for v in adjacencyList[u]: #u to v
		if v == endWord:
			pathTraversal[v] = u 
			queue = []
			break
		if v != u: #Because 4 repeats of word in adjacency list
			if dist[v] == float("inf"):
				pathTraversal[v] = u
				queue.append(v)
				dist[v] = dist[u] + 1

pathTravel = [endWord]

if endWord not in pathTraversal:
	print("Path is not found.")
else:
	nextWord = pathTravel[-1]
	while nextWord in pathTraversal:
		pathTravel += [pathTraversal[nextWord]]
		nextWord = pathTravel[-1]
	print(pathTravel[::-1])


