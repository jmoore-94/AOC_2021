with open('Day11.txt', 'r') as inputFile:
    p_input_lines = inputFile.readlines()
    p_input = [line.rstrip() for line in p_input_lines]


def parseInput(puzzle):
    for row in range(len(puzzle)):
        puzzle[row] = list(puzzle[row])
    return puzzle


def printOut(puzzle):
    for row in range(len(puzzle)):
        puzzle_row_string = ''.join(puzzle[row])
        print puzzle_row_string


def removeCoordinate(coordinate, coordinate_list):
    coordinate_list.remove(coordinate)
    return coordinate_list


def initialOctopusFlash(puzzle):
    coordinate_list = []
    count = 0
    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            if puzzle[row][column] == '9':
                coordinate_list.append([row, column])
                puzzle[row][column] = '0'
                count = count + 1
            else:
                puzzle[row][column] = str(int(puzzle[row][column]) + 1)
    # print coordinate_list
    return [coordinate_list, count]


def secondaryOctopusFlash(puzzle, coordinate, coordinate_list):
    count = 0
    if puzzle[coordinate[0]][coordinate[1]] == '9':
        puzzle[coordinate[0]][coordinate[1]] = '0'
        coordinate_list.append(coordinate)
        count = count + 1
    elif puzzle[coordinate[0]][coordinate[1]] == '0':
        pass
    else:
        puzzle[coordinate[0]][coordinate[1]] = str(int(puzzle[coordinate[0]][coordinate[1]]) + 1)
    return count


def findPuzzleAtStep(puzzle, coordinate_list, number):
    count = number
    num_rows = len(puzzle)
    num_columns = len(puzzle[0])
    keepGoing = True
    while keepGoing is True:
        for coordinate in coordinate_list:
            positionY = coordinate[0]
            positionX = coordinate[1]
            # Bottom Row
            if positionY == num_rows - 1:
                # Right Edge (3 neighbors to evaluate)
                if positionX == num_columns - 1:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX - 1], coordinate_list)
                # Left Edge (3 neighbors to evaluate)
                elif positionX == 0:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX + 1], coordinate_list)
                # Center (5 neighbors to evaluate)
                elif num_columns - 1 > positionX > 0:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX - 1], coordinate_list)
            # Top Row
            elif positionY == 0:
                # Right Edge (3 neighbors to evaluate)
                if positionX == num_columns - 1:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX - 1], coordinate_list)
                # Left Edge (3 neighbors to evaluate)
                elif positionX == 0:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX + 1], coordinate_list)
                # Center (5 neighbors to evaluate)
                elif num_columns - 1 > positionX > 0:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX - 1], coordinate_list)
            # Center Rows
            elif num_rows - 1 > positionY > 0:
                # Right Edge (5 neighbors to evaluate)
                if positionX == num_columns - 1:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX - 1], coordinate_list)
                # Left Edge (5 neighbors to evaluate)
                elif positionX == 0:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX + 1], coordinate_list)
                # Center (8 neighbors to evaluate)
                elif num_columns - 1 > positionX > 0:
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY + 1, positionX - 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX + 1], coordinate_list)
                    count = count + secondaryOctopusFlash(puzzle, [positionY - 1, positionX - 1], coordinate_list)
            removeCoordinate(coordinate, coordinate_list)
            if len(coordinate_list) < 1:
                keepGoing = False
    return count


steps = 500
answer = 0
p_input = parseInput(p_input)
for s in range(steps):
    printOut(p_input)
    count_flashes = 0
    octopus_effected_list = initialOctopusFlash(p_input)
    if len(octopus_effected_list[0]) > 0:
        count_flashes = findPuzzleAtStep(p_input, octopus_effected_list[0], octopus_effected_list[1])
    answer = answer + count_flashes
    print answer
    if count_flashes == 100:
        printOut(p_input)
        print 'DAY:' + str(s + 1)
        break

