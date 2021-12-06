# p_input = ['3,4,3,1,2']
p_input = ['3,5,3,5,1,3,1,1,5,5,1,1,1,2,2,2,3,1,1,5,1,1,5,5,3,2,2,5,4,4,1,5,1,4,4,5,2,4,1,1,5,3,1,1,4,1,1,1,1,4,1,1,1,1,2,1,1,4,1,1,1,2,3,5,5,1,1,3,1,4,1,3,4,5,1,4,5,1,1,4,1,3,1,5,1,2,1,1,2,1,4,1,1,1,4,4,3,1,1,1,1,1,4,1,4,5,2,1,4,5,4,1,1,1,2,2,1,4,4,1,1,4,1,1,1,2,3,4,2,4,1,1,5,4,2,1,5,1,1,5,1,2,1,1,1,5,5,2,1,4,3,1,2,2,4,1,2,1,1,5,1,3,2,4,3,1,4,3,1,2,1,1,1,1,1,4,3,3,1,3,1,1,5,1,1,1,1,3,3,1,3,5,1,5,5,2,1,2,1,4,2,3,4,1,4,2,4,2,5,3,4,3,5,1,2,1,1,4,1,3,5,1,4,1,2,4,3,1,5,1,1,2,2,4,2,3,1,1,1,5,2,1,4,1,1,1,4,1,3,3,2,4,1,4,2,5,1,5,2,1,4,1,3,1,2,5,5,4,1,2,3,3,2,2,1,3,3,1,4,4,1,1,4,1,1,5,1,2,4,2,1,4,1,1,4,3,5,1,2,1']

# # Part 1
# # This is not going to work for Part 2...Unless you want to wait all day...
# days = 80
# for i in p_input:
#     p_input = i.split(',')
# print p_input
#
# for d in range(days):
#     lanternfish_list = []
#     count_list = []
#     count = 0
#     for p in p_input:
#         if p != '0':
#             lanternfish = str(int(p) - 1)
#         elif p == '0':
#             lanternfish = '6'
#             count_list.append('8')
#         lanternfish_list.append(lanternfish)
#     lanternfish_list = lanternfish_list + count_list
#     p_input = lanternfish_list
#     print d
# print len(lanternfish_list)

# Part 2
def ParseInput(puzzle):
    for i in puzzle:
        puzzle = i.split(',')
    return puzzle


p_input = ParseInput(p_input)
days = 256

cycle_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
cycle_lanternfish_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for p in p_input:
    if p in cycle_list:
        cycle_lanternfish_list[int(p)] = cycle_lanternfish_list[int(p)] + 1
print p_input
for d in range(days):
    count = 0
    lanternfish_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(cycle_lanternfish_list)):
        if i == 0:
            lanternfish_reset = cycle_lanternfish_list[0]
            lanternfish_babies = cycle_lanternfish_list[0]
            lanternfish_list[8] = lanternfish_babies
        elif i != 0:
            lanternfish = cycle_lanternfish_list[i]
            if i == 7:
                lanternfish = lanternfish + lanternfish_reset
            lanternfish_list[i - 1] = lanternfish
    cycle_lanternfish_list = lanternfish_list
    for l in cycle_lanternfish_list:
        count = count + l
print 'Day:' + str(d), count
