# Reading in Data as .txt file
with open('Day09.txt', 'r') as inputFile:
    p_input_lines = inputFile.readlines()
    p_input = [line.rstrip() for line in p_input_lines]


def parseInput(puzzle):
    newPuzzle = []
    for p in puzzle:
        puzzle_row = []
        for r in p:
            puzzle_row.append(int(r))
        newPuzzle.append(puzzle_row)
    # print newPuzzle
    return newPuzzle


def compareAgainstNeighbors(puzzle, positionY, positionX):
    lowest_value = True
    element = puzzle[positionY][positionX]
    num_rows = len(puzzle)
    num_columns = len(puzzle[0])
    neighbor_list = []
    if positionX == num_columns - 1:
        neighbor_list.append(puzzle[positionY][positionX - 1])
    elif positionX == 0:
        neighbor_list.append(puzzle[positionY][positionX + 1])
    elif num_columns - 1 > positionX > 0:
        neighbor_list.append(puzzle[positionY][positionX - 1])
        neighbor_list.append(puzzle[positionY][positionX + 1])
    if positionY == num_rows - 1:
        neighbor_list.append(puzzle[positionY - 1][positionX])
    if positionY == 0:
        neighbor_list.append(puzzle[positionY + 1][positionX])
    elif num_rows - 1 > positionY > 0:
        neighbor_list.append(puzzle[positionY - 1][positionX])
        neighbor_list.append(puzzle[positionY + 1][positionX])
    for n in neighbor_list:
        if n <= element:
            lowest_value = False
    return lowest_value


# Part 2
def findBasinCoordinates(puzzle, positionY, positionX, coordinate_list):
    # print 'POINT: [' + str(positionY) + ',' + str(positionX) + ']'
    # print 'Y:' + str(positionY), 'X:' + str(positionX), 'Value:' + str(puzzle[positionY][positionX])
    num_rows = len(puzzle)
    num_columns = len(puzzle[0])
    basin_list = []
    if positionX == num_columns - 1:
        if puzzle[positionY][positionX - 1] < 9 and [positionX - 1, positionY] not in coordinate_list:
            basin_list.append([positionX - 1, positionY])
    elif positionX == 0:
        if puzzle[positionY][positionX + 1] < 9 and [positionX + 1, positionY] not in coordinate_list:
            basin_list.append([positionX + 1, positionY])
    elif num_columns - 1 > positionX > 0:
        if puzzle[positionY][positionX - 1] < 9 and [positionX - 1, positionY] not in coordinate_list:
            basin_list.append([positionX - 1, positionY])
        if puzzle[positionY][positionX + 1] < 9 and [positionX + 1, positionY] not in coordinate_list:
            basin_list.append([positionX + 1, positionY])
    if positionY == num_rows - 1:
        if puzzle[positionY - 1][positionX] < 9 and [positionX, positionY - 1] not in coordinate_list:
            basin_list.append([positionX, positionY - 1])
    elif positionY == 0:
        if puzzle[positionY + 1][positionX] < 9 and [positionX, positionY + 1] not in coordinate_list:
            basin_list.append([positionX, positionY + 1])
    elif num_rows - 1 > positionY > 0:
        if puzzle[positionY - 1][positionX] < 9 and [positionX, positionY - 1] not in coordinate_list:
            basin_list.append([positionX, positionY - 1])
        if puzzle[positionY + 1][positionX] < 9 and [positionX, positionY + 1] not in coordinate_list:
            basin_list.append([positionX, positionY + 1])
    return basin_list


p_input = parseInput(p_input)
risk_level = 0
basin_sizes = []
count = 1
for row in range(len(p_input)):
    for column in range(len(p_input[row])):
        if compareAgainstNeighbors(p_input, row, column) is True:
            # Storing points as X, Y
            point_list = [[column, row]]
            risk_level = risk_level + ((p_input[row][column]) + 1)
            add_on = True
            while add_on is True:
                additional_coordinates = []
                # print 'Point List: ' + str(point_list)
                for item in point_list:
                    coordinates = findBasinCoordinates(p_input, item[1], item[0], point_list)
                    additional_coordinates = additional_coordinates + coordinates
                    # print item, coordinates, additional_coordinates
                if len(additional_coordinates) > 0:
                    for a in range(len(additional_coordinates)):
                        if additional_coordinates[a] not in point_list:
                            point_list.append(additional_coordinates[a])
                else:
                    basin_sizes.append(len(point_list))
                    add_on = False
print risk_level
basin_sizes.sort(reverse=True)
basin_sizes = basin_sizes[:3]
for b in basin_sizes:
    count = count * int(b)
print basin_sizes, count



