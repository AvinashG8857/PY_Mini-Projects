import tkinter as tk

# Initialize board
board = [""] * 9

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def minimax(b, is_maximizing):
    winner = check_winner(b)
    if winner == "X": return -1
    if winner == "O": return 1
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -999
        for i in range(9):
            if b[i] == "":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 999
        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = ""
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -999
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")
    winner = check_winner(board)
    if winner:
        end_game(winner)

def player_move(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")
        winner = check_winner(board)
        if winner:
            end_game(winner)
        else:
            ai_move()

def end_game(winner):
    if winner == "Draw":
        result_label.config(text="It's a Draw!")
    else:
        result_label.config(text=f"{winner} Wins!")
    for btn in buttons:
        btn.config(state="disabled")

def restart():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Tic Tac Toe with AI")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: player_move(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.grid(row=3, column=0, columnspan=3)

restart_button = tk.Button(root, text="Restart", command=restart)
restart_button.grid(row=4, column=0, columnspan=3)

root.mainloop()