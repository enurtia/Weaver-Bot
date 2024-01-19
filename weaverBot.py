import numpy as np 


#Letter our 4-letter wordlist
words = np.loadtxt("4LetterWords.txt", dtype=str)
words = np.char.lower(words)

startWord = input("Start word: ").lower()
endWord = input("End Word: ").lower()


#Create adjacency list
dist = {}
adjacencyList = {}
for word in words:
	dist[word] = float("inf")
	adjacencyList[word] = []
	for w in words:
		difCount = 0
		for i in range(4):
			if(w[i] != word[i]):
				difCount += 1
		if difCount == 1:
			adjacencyList[word] += [w]


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
