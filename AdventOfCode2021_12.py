from collections import Counter

with open('Day12.txt', 'r') as inputFile:
    p_input_lines = inputFile.readlines()
    p_input = [line.rstrip() for line in p_input_lines]


def parseInput(puzzle):
    for row in range(len(puzzle)):
        puzzle[row] = puzzle[row].split('-')


# Create dictionary 'Cave' as key 'Potential Path' as values
pathways = {}
for p in p_input:
    startPoint, endPoint = p.split('-')
    if startPoint in pathways:
        pathways[startPoint].append(endPoint)
    elif startPoint not in pathways:
        pathways[startPoint] = [endPoint]
    if endPoint in pathways:
        pathways[endPoint].append(startPoint)
    elif endPoint not in pathways:
        pathways[endPoint] = [startPoint]
print pathways


def numberOfTimesASmallCaveWasVisited(currPath):
    numLowerCase = []
    for c in currPath:
        if c.islower():
            numLowerCase.append(c)
    count_numLowerCase = Counter(numLowerCase)
    count_numLowerCase = count_numLowerCase.values()
    count_numLowerCase.sort(reverse=True)
    # Part 1 
    if count_numLowerCase[0] <= 1:
        return True
    # Part 2
    # count_visits = count_numLowerCase.count(2)
    # if count_numLowerCase[0] <= 2 and count_visits <= 1:
    #     return True
    return False


def checkPath(specificPath, location):
    # Cannot go backwards to start once you've left start
    if specificPath == "start":
        return False
    # Check if path is uppercase, can visit as many times as necessary
    if specificPath.isupper():
        return True
    # Check if path is lowercase, can visit 1 cave twice, but all other lowercase caves once
    elif specificPath.islower():
        if numberOfTimesASmallCaveWasVisited(location) is True:
            return True
    return False


paths = [["start"]]
numberOfPaths = 0
while len(paths) > 0:
    currentPath = paths.pop()
    if currentPath[-1] == "end":
        print(",".join(currentPath))
        numberOfPaths = numberOfPaths + 1
        continue
    for p in pathways[currentPath[-1]]:
        if checkPath(p, currentPath):
            newPath = list(currentPath)
            newPath.append(p)
            paths.append(newPath)
print numberOfPaths
