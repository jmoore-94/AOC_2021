with open('Day13.txt', 'r') as inputFile:
    p_input_lines = inputFile.readlines()
    p_input = [line.rstrip() for line in p_input_lines]


def parseInput(puzzle, returnType=None):
    coordinates = []
    instructions = []
    for p in puzzle:
        if 'fold' in p:
            instruction = p
            instruction = instruction.replace('fold along ', '')
            instructions.append(instruction)
        elif p == '':
            pass
        else:
            coordinate = p.split(',')
            coordinate[0] = int(coordinate[0])
            coordinate[1] = int(coordinate[1])
            coordinates.append((coordinate[0], coordinate[1]))
    if returnType is 'instruction':
        return instructions
    if returnType is 'coordinate':
        return coordinates


def findPaperSize(coordinates):
    max_Y = 0
    max_X = 0
    for coord in coordinates:
        if coord[1] > max_Y:
            max_Y = coord[1]
        if coord[0] > max_X:
            max_X = coord[0]
    print max_Y + 1, max_X + 1
    # Max row and column are one less than total size
    return [max_Y + 1, max_X + 1]


def createPaper(size, coordinates):
    paper = []
    for y in range(size[0]):
        paper.append(['.'])
        # One less to append because the first element was appended in Y
        for x in range(size[1] - 1):
            paper[y].append('.')
    for c in coordinates:
        paper[c[1]][c[0]] = '#'
    return paper


def foldPaper(paper, instruction):
    paperA = []
    paperB = []
    paperB_temp = []
    if 'x' in instruction:
        print 'HOT DOG STYLE'
        fold_line = instruction.replace('x=', '')
        for row in range(len(paper)):
            paperA.append(paper[row][:int(fold_line)])
            paperB_temp.append(paper[row][::-1])
            paperB.append(paperB_temp[row][:int(fold_line)])
    elif 'y' in instruction:
        print 'HAMBURGER STYLE'
        fold_line = instruction.replace('y=', '')
        paperA = paper[:int(fold_line)]
        paperB_temp = paper[int(fold_line) + 1:]
        for b in range(len(paperB_temp) - 1, -1, -1):
            paperB.append(paperB_temp[b])
    folded_paper = paperA
    for row in range(len(paperA)):
        for column in range(len(paperA[row])):
            if paperA[row][column] == '.' and paperB[row][column] == '#':
                folded_paper[row][column] = '#'
            else:
                pass
    return folded_paper


def printOut(paper):
    count = 0
    for p in paper:
        print ''.join(p)
        count += p.count('#')
    print 'Total Dots:', count


coordinate_list = parseInput(p_input, returnType='coordinate')
instruction_list = parseInput(p_input, returnType='instruction')
paperSize = findPaperSize(coordinate_list)
fullPaper = createPaper(paperSize, coordinate_list)
printOut(fullPaper)
# # Part 1
# oneFold = foldPaper(fullPaper, instruction_list[0])
# printOut(oneFold)
# Part 2
fold = fullPaper
for i in instruction_list:
    fold = foldPaper(fold, i)
    printOut(fold)
    