import sys

def read_board_from_file(filename):
    with open(filename, 'r') as f:
        board = [list(line.strip()) for line in f if line.strip()]
    return board

def find_king(board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 'K':
                return x, y
    return None

def is_check_by_pawn(x, y, board):
    directions = [(-1, -1), (1, -1)]  # Pawn เดินขึ้น
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
            if board[ny][nx] == 'P':
                return True
    return False

def is_check_by_rook(x, y, board):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if not (0 <= ny < len(board) and 0 <= nx < len(board[0])):
                break
            if board[ny][nx] != '.':
                if board[ny][nx] == 'R':
                    return True
                break
    return False

def king_in_check(board):
    k_pos = find_king(board)
    if not k_pos:
        return None
    x, y = k_pos
    return is_check_by_pawn(x, y, board) or is_check_by_rook(x, y, board)

def check_board(filename):
    try:
        board = read_board_from_file(filename)
    except FileNotFoundError:
        print(f"❌ {filename}: File not found")
        return

    # ตรวจว่าทุกแถวมีขนาดเท่ากัน
    row_len = len(board[0])
    if any(len(row) != row_len for row in board):
        print(f"❌ {filename}: Invalid board shape (uneven rows)")
        return

    check = king_in_check(board)
    if check is None:
        print(f"❌ {filename}: No King found")
    elif check:
        print(f"🛑 {filename}: King is in check")
    else:
        print(f"✅ {filename}: King is safe")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("📂 Usage: python3 main.py file1.chess file2.chess ...")
    else:
        for file in sys.argv[1:]:
            check_board(file)
