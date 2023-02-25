# input exam:
"""
0,0,0,0,4,0,0,9,0
0,0,0,0,2,3,0,0,0
9,5,0,0,0,0,0,0,3
0,0,3,0,0,0,0,0,0
4,0,0,1,0,7,0,5,2
0,0,5,0,8,0,3,0,0
2,9,0,4,1,0,0,0,0
0,0,1,0,0,9,0,8,4
8,0,0,0,0,0,0,2,0
"""

"""
0,9,0,0,0,0,0,7,0
0,0,2,0,0,9,4,1,0
6,0,0,0,0,0,0,0,0
0,0,9,3,0,0,0,0,0
5,0,0,0,7,0,2,0,0
8,0,0,9,0,0,0,0,0
9,0,0,0,5,0,0,0,0
2,0,0,1,9,6,5,4,0
0,0,6,0,3,0,7,0,1
"""

# The hardest Sudoku in the world (about 3 min runnig):
"""
8,0,0,0,0,0,0,0,0
0,0,3,6,0,0,0,0,0
0,7,0,0,9,0,2,0,0
0,5,0,0,0,7,0,0,0
0,0,0,0,4,5,7,0,0
0,0,0,1,0,0,0,3,0
0,0,1,0,0,0,0,6,8
0,0,8,5,0,0,0,1,0
0,9,0,0,0,0,4,0,0
"""



def len1_neighbor(i, j, m, n, sodoco):
    if type(sodoco[m][n]) == list and sodoco[i][j] in sodoco[m][n]:
        sodoco[m][n].remove(sodoco[i][j])
        if len(sodoco[m][n]) == 1:
            sodoco = len1(m, n, sodoco)
    return sodoco


def len1(row, column, sodoco):
    if type(sodoco[row][column]) != list or len(sodoco[row][column]) != 1:
        return False

    sodoco[row][column] = sodoco[row][column][0]
    for k in range(0, 9):
        sodoco = len1_neighbor(row, column, k, column, sodoco)
        sodoco = len1_neighbor(row, column, row, k, sodoco)

    for m in range(0, 9):
        for n in range(0, 9):
            if int(m / 3) == int(row / 3) and int(n / 3) == int(column / 3):
                sodoco = len1_neighbor(row, column, m, n, sodoco)

    return sodoco


def work_sodoco(sodoco):
    edits = True
    while edits != 0:

        edits = 0

        for row in range(0, 9):
            for num in range(1, 10):
                repeat = 0
                place = []
                for column in range(0, 9):
                    if type(sodoco[row][column]) == str and str(num) == sodoco[row][column]:
                        repeat = 0
                        break
                    if type(sodoco[row][column]) == list and str(num) in sodoco[row][column]:
                        repeat += 1
                        place.append(column)

                if repeat == 1:
                    edits += 1
                    sodoco[row][place[0]] = [str(num)]
                    sodoco = len1(row, place[0], sodoco)

                if repeat > 1:
                    ok = True
                    for i in place:
                        if int(place[0] / 3) != int(i / 3):
                            ok = False
                            break
                    if ok:
                        for a in [3 * int(row / 3), 3 * int(row / 3) + 1, 3 * int(row / 3) + 2]:
                            for b in [3 * int(place[0] / 3), 3 * int(place[0] / 3) + 1, 3 * int(place[0] / 3) + 2]:
                                if type(sodoco[a][b]) == list and str(num) in sodoco[a][b]:
                                    if not (a == row and b in place):
                                        sodoco[a][b].remove(str(num))
                                        edits += 1
                                        if len(sodoco[a][b]) == 1:
                                            sodoco = len1(a, b, sodoco)

        # ---------------------------------------

        for column in range(0, 9):
            for num in range(1, 10):
                repeat = 0
                place = []
                for row in range(0, 9):
                    if type(sodoco[row][column]) == str and str(num) == sodoco[row][column]:
                        repeat = 0
                        break
                    if type(sodoco[row][column]) == list and str(num) in sodoco[row][column]:
                        repeat += 1
                        place.append(row)

                if repeat == 1:
                    edits += 1
                    sodoco[place[0]][column] = [str(num)]
                    sodoco = len1(place[0], column, sodoco)

                if repeat > 1:
                    ok = True
                    for i in place:
                        if int(place[0] / 3) != int(i / 3):
                            ok = False
                            break
                    if ok:
                        for a in [3 * int(column / 3), 3 * int(column / 3) + 1, 3 * int(column / 3) + 2]:
                            for b in [3 * int(place[0] / 3), 3 * int(place[0] / 3) + 1, 3 * int(place[0] / 3) + 2]:
                                if type(sodoco[b][a]) == list and str(num) in sodoco[b][a]:
                                    if not (a == column and b in place):
                                        sodoco[b][a].remove(str(num))
                                        edits += 1
                                        if len(sodoco[b][a]) == 1:
                                            sodoco = len1(b, a, sodoco)

        # ------------------------------------------

        for m in [0, 3, 6]:
            for n in [0, 3, 6]:
                for i in range(1, 10):
                    rep = 0
                    l = [[], []]
                    for j in range(0, 3):
                        br = False
                        for k in range(0, 3):
                            if type(sodoco[j + n][k + m]) == str and str(i) == sodoco[j + n][k + m]:
                                rep = 0
                                br = True
                                break
                            if type(sodoco[j + n][k + m]) == list and str(i) in sodoco[j + n][k + m]:
                                rep += 1
                                l[0].append(j + n)
                                l[1].append(k + m)
                        if br:
                            break

                    if rep == 1:
                        edits += 1
                        sodoco[l[0][0]][l[1][0]] = [str(i)]
                        sodoco = len1(l[0][0], l[1][0], sodoco)

                    if rep > 1:
                        oki = True
                        okj = True
                        for a in l[0]:
                            if l[0][0] != a:
                                oki = False
                        for b in l[1]:
                            if l[1][0] != b:
                                okj = False
                        if oki:
                            for a in range(0, 9):
                                if type(sodoco[l[0][0]][a]) == list and str(i) in sodoco[l[0][0]][a]:
                                    if 3 * int(a / 3) != m:
                                        sodoco[l[0][0]][a].remove(str(i))
                                        edits += 1
                                        if len(sodoco[l[0][0]][a]) == 1:
                                            sodoco = len1(l[0][0], a, sodoco)

                        if okj:
                            for a in range(0, 9):
                                if type(sodoco[a][l[1][0]]) == list and str(i) in sodoco[a][l[1][0]]:
                                    if 3 * int(a / 3) != n:
                                        sodoco[a][l[1][0]].remove(str(i))
                                        edits += 1
                                        if len(sodoco[a][l[1][0]]) == 1:
                                            sodoco = len1(a, l[1][0], sodoco)

    # ---------------------------------------------

    for i in range(0, 9):
        x = []
        y = []
        for j in range(0, 9):
            if type(sodoco[i][j]) == str and sodoco[i][j] != 'x':
                if sodoco[i][j] in x:
                    return False
                else:
                    x.append(sodoco[i][j])
            if type(sodoco[j][i]) == str and sodoco[j][i] != 'x':
                if sodoco[j][i] in y:
                    return False
                else:
                    y.append(sodoco[j][i])

    for m in [0, 3, 6]:
        for n in [0, 3, 6]:
            x = []
            for i in range(0, 3):
                for j in range(0, 3):
                    if type(sodoco[i + m][j + n]) == str and sodoco[i + m][j + n] != 'x':
                        if sodoco[i + m][j + n] in x:
                            return False
                        else:
                            x.append(sodoco[i + m][j + n])

    return sodoco


# -------------------------------------------------------

def print_sodoco(sodoco):
    for i in range(0, 9):
        for j in range(0, 9):
            print(' | ' + sodoco[i][j], end='')
        print(' |')


# -------------------------------------------------------


sodoco = [input().split(',')]
for i in range(0, 8):
    sodoco.append(input().split(','))

print('Array of sudoko:')
print(sodoco)

thirdD = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(0, 9):
    for j in range(0, 9):
        if sodoco[i][j] == '0':
            m = thirdD.copy()
            for k in range(0, 9):
                if type(sodoco[k][j]) == str and sodoco[k][j] != '0' and sodoco[k][j] in m:
                    m.remove(sodoco[k][j])
                if type(sodoco[i][k]) == str and sodoco[i][k] != '0' and sodoco[i][k] in m:
                    m.remove(sodoco[i][k])
                for l in range(0, 9):
                    if int(k / 3) == int(i / 3) and int(l / 3) == int(j / 3) and type(sodoco[k][l]) == str and \
                            sodoco[k][l] != '0' and sodoco[k][l] in m:
                        m.remove(sodoco[k][l])

            sodoco[i][j] = m

for i in range(0, 9):
    for j in range(0, 9):
        if type(sodoco[i][j]) != str and len(sodoco[i][j]) == 1:
            sodoco = len1(i, j, sodoco)

sodoco = work_sodoco(sodoco)
sodocos = [sodoco]
indexes = []
suspect = []
select = []
Number_answer = 0

a = 0
b = []
for i in range(0, 9):
    for j in range(0, 9):
        if type(sodoco[i][j]) == list:
            if len(sodoco[i][j]) > a:
                a = len(sodoco[i][j])
                b = [i, j, sodoco[i][j]]

if a < 10:
    print('Answers:---------------------------------------------')
    while True:
        # print(suspect)
        if sodocos[-1]:
            a = 0
            b = []
            for i in range(0, 9):
                for j in range(0, 9):
                    if type(sodocos[-1][i][j]) == list:
                        if len(sodocos[-1][i][j]) > a:
                            a = len(sodocos[-1][i][j])
                            b = [i, j, sodocos[-1][i][j]]

            if a == 0:
                print_sodoco(sodocos[-1])
                # for i in range(0, 9):
                #     print(sodocos[-1][i])
                print('----------------------------------------------')
                Number_answer += 1
                # -----------------------------------
                for g in range(0, len(suspect))[::-1]:
                    if len(suspect[-1]) == 1:
                        suspect.pop()
                        indexes.pop()
                        select.pop()
                        sodocos.pop()
                    else:
                        suspect[-1].pop()
                        select[-1] = suspect[-1][-1]
                        sodocos.pop()
                        sodoco1 = []

                        for i in range(0, 9):
                            sodoco1.append([])
                            for j in range(0, 9):
                                if type(sodocos[-1][i][j]) == list:
                                    sodoco1[i].append(sodocos[-1][i][j].copy())
                                else:
                                    sodoco1[i].append(sodocos[-1][i][j])

                        sodoco1[indexes[-1][0]][indexes[-1][1]] = suspect[-1][-1]
                        sodocos.append(work_sodoco(sodoco1))
                        break
                # -------------------------------------------

            else:
                suspect.append(b[2])
                indexes.append(b[0:2])
                select.append(b[2][-1])
                sodoco1 = []

                for i in range(0, 9):
                    sodoco1.append([])
                    for j in range(0, 9):
                        if type(sodocos[-1][i][j]) == list:
                            sodoco1[i].append(sodocos[-1][i][j].copy())
                        else:
                            sodoco1[i].append(sodocos[-1][i][j])

                sodoco1[b[0]][b[1]] = suspect[-1][-1]
                sodocos.append(work_sodoco(sodoco1))
        else:
            for g in range(0, len(suspect))[::-1]:
                if len(suspect[-1]) == 1:
                    suspect.pop()
                    indexes.pop()
                    select.pop()
                    sodocos.pop()
                else:
                    suspect[-1].pop()
                    select[-1] = suspect[-1][-1]
                    sodocos.pop()
                    sodoco1 = []

                    for i in range(0, 9):
                        sodoco1.append([])
                        for j in range(0, 9):
                            if type(sodocos[-1][i][j]) == list:
                                sodoco1[i].append(sodocos[-1][i][j].copy())
                            else:
                                sodoco1[i].append(sodocos[-1][i][j])

                    sodoco1[indexes[-1][0]][indexes[-1][1]] = suspect[-1][-1]
                    sodocos.append(work_sodoco(sodoco1))
                    break
        if len(suspect) == 0:
            break
    print('Number of answers:', Number_answer)

else:
    for i in range(0, 9):
        print(sodoco[i])
    print('Number of answers: 1')
