from collections import Counter

with open('Day14_Test.txt', 'r') as inputFile:
    p_input_lines = inputFile.readlines()
    p_input = [line.rstrip() for line in p_input_lines]


def parseInput(puzzle, returnType=None):
    startingPoint = []
    rules = []
    for p in range(len(puzzle)):
        if puzzle[p] is '':
            startingPoint = puzzle[0]
            rules = puzzle[p + 1:]
    if returnType is 'startingPoint':
        return startingPoint
    elif returnType is 'rules':
        for r in range(len(rules)):
            rules[r] = rules[r].split(' -> ')
        return rules


def findRule(match, rules):
    for r in rules:
        if match in r:
            return r


def processInitialData(start):
    print start
    collectPairs = {}
    for i in range(1, len(start)):
        findPair = start[i - 1] + start[i]
        if findPair not in collectPairs:
            collectPairs[findPair] = 1
        elif findPair in collectPairs:
            collectPairs[findPair] = collectPairs[findPair] + 1
    print collectPairs
    return collectPairs


def processSecondaryData(pairs, rules):
    key_list = pairs.keys()
    additionalPairs = []
    for key in key_list:
        relevantRule = findRule(key, rules)
        amount = pairs[key]
        characterA = relevantRule[0][0] + relevantRule[1]
        characterB = relevantRule[1] + relevantRule[0][1]
        pairs[key] = pairs[key] - amount
        additionalPairs.append([characterA, amount])
        additionalPairs.append([characterB, amount])
    for add in additionalPairs:
        if add[0] in pairs:
            pairs[add[0]] = pairs[add[0]] + add[1]
        elif add[0] not in pairs:
            pairs[add[0]] = add[1]
    return pairs


def calculateOccurrences(pairs, initialTemplate):
    countOccurrences = {}
    print initialTemplate
    for key in pairs:
        if key[0] not in countOccurrences:
            countOccurrences[key[0]] = pairs[key]
        elif key[0] in countOccurrences:
            countOccurrences[key[0]] = countOccurrences[key[0]] + pairs[key]
        if key[1] not in countOccurrences:
            countOccurrences[key[1]] = pairs[key]
        elif key[1] in countOccurrences:
            countOccurrences[key[1]] = countOccurrences[key[1]] + pairs[key]
    # Keeping track of pairs counts each letter twice
    for occurrence in countOccurrences:
        countOccurrences[occurrence] = countOccurrences[occurrence] / 2
        # First and Last character of the initial Template never change
        # Add one to their occurrences
        if occurrence == initialTemplate[0] or occurrence == initialTemplate[-1]:
            countOccurrences[occurrence] = countOccurrences[occurrence] + 1
    maxOccurrence = max(countOccurrences.values())
    minOccurrence = min(countOccurrences.values())
    return maxOccurrence - minOccurrence


puzzleTemplate = parseInput(p_input, returnType='startingPoint')
puzzleRules = parseInput(p_input, returnType='rules')
print puzzleTemplate
print puzzleRules

stepCount = 40
newTemplate = processInitialData(puzzleTemplate)
for s in range(stepCount):
    newTemplate = processSecondaryData(newTemplate, puzzleRules)
    print s + 1, newTemplate

print calculateOccurrences(newTemplate, puzzleTemplate)
