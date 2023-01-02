puzzle = """
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
"""
# solve this sudoku then the others
oglist = []
editlist = []
k = 0
for i in range(0,9):
    for j in range(0,9):
        k += 1
        oglist.append(puzzle[k])
        editlist.append(puzzle[k])
    k += 1

def error(list):
    check = []
    for i in range(0,9):
        check.append(list[i])
    

index = -1
while True:
    index += 1
    if editlist[index] == 0:
        editlist[index] += 1
    