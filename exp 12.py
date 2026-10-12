WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]


def print_board(b):
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(b[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def winner(b):
    for x, y, z in WIN_LINES:
        if b[x] != " " and b[x] == b[y] == b[z]:
            return b[x]
    return None


def minimax(b, player):
    """Score from O's point of view: +1 O wins, -1 X wins, 0 draw."""
    w = winner(b)
    if w == "O":
        return 1
    if w == "X":
        return -1
    if " " not in b:
        return 0
    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = player
            scores.append(minimax(b, "X" if player == "O" else "O"))
            b[i] = " "
    return max(scores) if player == "O" else min(scores)


def best_move(b, player):
    best, move = None, None
    for i in range(9):
        if b[i] == " ":
            b[i] = player
            score = minimax(b, "X" if player == "O" else "O")
            b[i] = " "
            if player == "X":
                score = -score
            if best is None or score > best:
                best, move = score, i
    return move


def play(demo=False):
    board = [" "] * 9
    player = "X"
    print("Positions are numbered 1-9, left to right, top to bottom.")
    while True:
        print_board(board)
        if winner(board) or " " not in board:
            break
        if player == "X" and not demo:
            while True:
                try:
                    m = int(input("Your move (1-9): ")) - 1
                    if 0 <= m < 9 and board[m] == " ":
                        break
                except ValueError:
                    pass
                print("Invalid move, try again.")
        else:
            m = best_move(board, player)
            print(f"Computer ({player}) plays {m + 1}")
        board[m] = player
        player = "O" if player == "X" else "X"

    w = winner(board)
    print(f"Winner: {w}" if w else "It's a draw!")


play()
