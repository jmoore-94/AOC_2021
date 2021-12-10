with open('Day10.txt', 'r') as inputFile:
    p_input_lines = inputFile.readlines()
    p_input = [line.rstrip() for line in p_input_lines]


def findMatch(openCharacter):
    if openCharacter == '[':
        closedCharacter = ']'
    elif openCharacter == '(':
        closedCharacter = ')'
    elif openCharacter == '<':
        closedCharacter = '>'
    elif openCharacter == '{':
        closedCharacter = '}'
    return closedCharacter


def checkMatch(openCharacter, closedCharacter):
    if openCharacter == '[' and closedCharacter == ']':
        match = True
    elif openCharacter == '(' and closedCharacter == ')':
        match = True
    elif openCharacter == '<' and closedCharacter == '>':
        match = True
    elif openCharacter == '{' and closedCharacter == '}':
        match = True
    else:
        match = False
    return match


def checkOpenClose(puzzle_list, character):
    if checkMatch(puzzle_list[-1], character) is True:
        puzzle_list = puzzle_list[:-1]
        return puzzle_list
    else:
        expectedCharacter = findMatch(puzzle_list[-1])
        invalid_string = 'Expected: ' + expectedCharacter + ' Found: ' + character
        print invalid_string
        return character


def tallyValue(solution_list):
    print solution_list
    tally = 0
    count = 0
    for s in solution_list:
        if s == ']':
            tally = 57
        elif s == ')':
            tally = 3
        elif s == '>':
            tally = 25137
        elif s == '}':
            tally = 1197
        count = count + tally
    return count


def evaluateScore(score_list):
    count = 0
    for s in score_list:
        count = count * 5
        if s == ']':
            count = count + 2
        elif s == ')':
            count = count + 1
        elif s == '>':
            count = count + 4
        elif s == '}':
            count = count + 3
    return count


invalid_list = []
incomplete_scores = []
for puzzle in p_input:
    invalid = False
    storage_list = []
    incomplete_list = []
    for p in puzzle:
        if p == '[' or p == '(' or p == '<' or p == '{':
            storage_list.append(p)
        else:
            catch = checkOpenClose(storage_list, p)
            if type(catch) is str:
                invalid_list.append(catch)
                invalid = True
            else:
                storage_list = catch
        if invalid is True:
            break
    if invalid is False:
        storage_list.reverse()
        for item in storage_list:
            i = findMatch(item)
            incomplete_list.append(i)
        score = evaluateScore(incomplete_list)
        incomplete_scores.append(score)
incomplete_scores.sort()
score_index = ((len(incomplete_scores)) - 1) / 2
print tallyValue(invalid_list)
print incomplete_scores[score_index]
