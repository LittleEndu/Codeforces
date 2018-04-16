# Tries: 1
rows = int(input())
boards = []
board = ""
for i in range(4 * rows + 3):
    line = input()
    if not line:
        boards.append(board)
        board = ""
    else:
        board += line
boards.append(board)


def difference(board_in, type=0):
    to_return = 0
    for i in board_in:
        to_return += int(i != str(type))
        type = (type + 1) % 2
    return to_return


zero_board_diff = [difference(i, 0) for i in boards]
one_board_diff = [rows ** 2 - i for i in zero_board_diff]
possibilities = []

for i in range(4):
    for j in range(4):
        if i == j:
            continue
        ones = [0, 1, 2, 3]
        ones.remove(i)
        ones.remove(j)
        possibilities.append(zero_board_diff[i] +
                             zero_board_diff[j] +
                             one_board_diff[ones[0]] +
                             one_board_diff[ones[1]]
                             )

print(sorted(possibilities)[0])
