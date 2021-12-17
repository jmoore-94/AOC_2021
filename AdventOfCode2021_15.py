import networkx as netx

with open('Day15.txt', 'r') as inputFile:
    p_input_lines = inputFile.readlines()
    p_input = [line.rstrip() for line in p_input_lines]

# print p_input
for p in p_input:
    print p

# Part 1
def buildGraph(puzzle):
    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            start = '(' + str(row) + ', ' + str(column) + ')'
            value = int(puzzle[row][column])
            if column <= numberOfColumns - 1:
                endH = '(' + str(row) + ', ' + str(column + 1) + ')'
                valueH = int(puzzle[row][column + 1])
                killmeGraph.add_weighted_edges_from([(start, endH, valueH), (endH, start, value)])
                print start, endH, valueH
            if row <= numberOfRows - 1:
                endV = '(' + str(row + 1) + ', ' + str(column) + ')'
                valueV = int(puzzle[row + 1][column])
                print start, endV, valueV
                killmeGraph.add_weighted_edges_from([(start, endV, valueV), (endV, start, value)])
    # print killmeGraph.nodes
    # print killmeGraph.edges


# Part 2
def buildLargeCave(puzzle):
    numberOfTimes = len(puzzle)
    for rows in range(len(puzzle)):
        newPuzzleRow = []
        for r in range(4):
            newPuzzleLine = []
            for element in range(len(puzzle[rows])):
                evaluateElement = (int(puzzle[rows][element]) + r + 1)
                if evaluateElement > 9:
                    evaluateElement = evaluateElement % 9
                newPuzzleLine.append(str(evaluateElement))
            newPuzzleRow.append(''.join(newPuzzleLine))
        for n in newPuzzleRow:
            puzzle[rows] = puzzle[rows] + n
    for again in range(4):
        newLine = []
        for lineR in range(numberOfTimes):
            evaluateLine = []
            for item in puzzle[lineR]:
                evaluateElement = (int(item) + again + 1)
                if evaluateElement > 9:
                    evaluateElement = evaluateElement % 9
                evaluateLine.append(str(evaluateElement))
            newLine.append(''.join(evaluateLine))
        puzzle = puzzle + newLine
    return puzzle


killmeGraph = netx.DiGraph()
p_input = buildLargeCave(p_input)
numberOfRows = len(p_input) - 1
numberOfColumns = len(p_input[0]) - 1
buildGraph(p_input)
endPoint = '(' + str(numberOfRows) + ', ' + str(numberOfColumns) + ')'
shortestPath = netx.dijkstra_path(killmeGraph, '(0, 0)', endPoint)
print shortestPath
count = 0
for s in shortestPath:
    s = s[1: -1]
    s = s.split(', ')
    row = int(s[0])
    column = int(s[1])
    if row == 0 and column == 0:
        pass
    else:
        count += int(p_input[row][column])
print len(shortestPath)
print count


