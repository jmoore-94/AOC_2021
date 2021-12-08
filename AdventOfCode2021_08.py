# Reading in Data as .txt file
with open('Day08.txt', 'r') as inputFile:
    p_input = inputFile.read()


def ParseInput(puzzle):
    newPuzzle = []
    newPuzzle_segment = ''
    newPuzzle_list = []
    for p in range(len(puzzle)):
        if puzzle[p] == '|' and puzzle[p + 1] == ' ':
            newPuzzle_list.append('')
        elif puzzle[p] == ' ' and puzzle[p - 1] == '|':
            pass
        elif puzzle[p] == '\n':
            newPuzzle_list.append(newPuzzle_segment)
            newPuzzle.append(newPuzzle_list)
            newPuzzle_segment = ''
            newPuzzle_list = []
        elif puzzle[p] != ' ':
            newPuzzle_segment = newPuzzle_segment + puzzle[p]
        elif puzzle[p] == ' ':
            newPuzzle_list.append(newPuzzle_segment)
            newPuzzle_segment = ''
    newPuzzle_list.append(newPuzzle_segment)
    newPuzzle.append(newPuzzle_list)
    return newPuzzle


p_input = ParseInput(p_input)

# Part 1
# output_list = []
# for line in p_input:
#     print line
#     for (index, l) in enumerate(line):
#         if l == '':
#             output_list = output_list + (line[index + 1:])
# print output_list
# count = 0
# for o in output_list:
#     if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
#         count = count + 1
# print count

# Part 2
def sortString(string):
    newString = ''
    parsedString = []
    for s in string:
        parsedString.append(s)
    parsedString.sort()
    for s in parsedString:
        newString = newString + s
    return newString


def checkForMatch(checkString, match):
    count = 0
    check = []
    for c in checkString:
        check.append(c)
    for m in match:
        if m in check:
            count = count + 1
    if count == len(match):
        return True
    else:
        return False


def checkForMisMatch(checkString, match):
    count = 0
    check = []
    matchcheck = []
    for c in checkString:
        check.append(c)
    for m in match:
        matchcheck.append(m)
    for item in check:
        if item not in matchcheck:
            count = count + 1
    return count


def findValue(string, solutionKey):
    value = ''
    for item in solutionKey:
        if string in item and len(string) == (len(item) - 2):
            value = item[0]
    return value


input_list = []
output_list = []
solved = []
for line in p_input:
    for (index, l) in enumerate(line):
        if l == '':
            output_list.append(line[index + 1:])
            input_list.append(line[0:index])
for l_input in input_list:
    Done = False
    solved_list = ['', '', '', '', '', '', '', '', '', '']
    while Done is False:
        for i in l_input:
            i = sortString(i)
            # Find #1
            if len(i) == 2 and '1:' not in solved_list[1]:
                solved_list[1] = ('1:' + i)
            # Find #4
            if len(i) == 4 and '4:' not in solved_list[4]:
                solved_list[4] = ('4:' + i)
            # Find #7
            if len(i) == 3 and '7:' not in solved_list[7]:
                solved_list[7] = ('7:' + i)
            # Find #8
            if len(i) == 7 and '8:' not in solved_list[8]:
                solved_list[8] = ('8:' + i)
            # Find #3
            if len(i) is 5 and '7:' in solved_list[7]:
                # Match against #7, since all elements from #7 are in #3, and no other 5 element numbers
                matchString = solved_list[7][2:]
                if checkForMatch(i, matchString) is True and '3:' not in solved_list[3]:
                    solved_list[3] = ('3:' + i)
            # Find #2
            if len(i) is 5 and '1:' in solved_list[1] and '4:' in solved_list[4] and '7:' in solved_list[7]:
                # Using #1, #4, and #7, #2 is the only 5 element number that has 2 elements not in common with these combined
                matchString = solved_list[1][2:] + solved_list[4][2:] + solved_list[7][2:]
                if checkForMisMatch(i, matchString) == 2 and '2:' not in solved_list[2]:
                    solved_list[2] = ('2:' + i)
            # Find #5
            if len(i) is 5 and i not in solved_list[2] and i not in solved_list[3]:
                # Only 5 element number remaining by process of elimination
                solved_list[5] = ('5:' + i)
            # Find #9
            if len(i) is 6 and '3:' in solved_list[3]:
                # Match against #3, since all elements from #3 are in #9, and no other 6 element numbers
                matchString = solved_list[3][2:]
                if checkForMatch(i, matchString) is True and '9:' not in solved_list[9]:
                    solved_list[9] = ('9:' + i)
            # Find #6
            if len(i) is 6 and '7:' in solved_list[7]:
                # Match against #7, since all elements from #7 are in #0 and #9, but not #6
                matchString = solved_list[7][2:]
                if checkForMatch(i, matchString) is False and '6:' not in solved_list[6]:
                    solved_list[6] = ('6:' + i)
            # Find #0
            if len(i) is 6 and i not in solved_list[6] and i not in solved_list[9]:
                # Only 6 element number remaining by process of elimination
                solved_list[0] = ('0:' + i)
        # All keys have been found
        if '' not in solved_list:
            Done = True
            # Put key in list that matches the output_list order (to call later)
            solved.append(solved_list)
count = 0
for output in range(len(output_list)):
    answer = ''
    for o in output_list[output]:
        o = sortString(o)
        answer = answer + findValue(o, solved[output])
    count = count + int(answer)
print count








