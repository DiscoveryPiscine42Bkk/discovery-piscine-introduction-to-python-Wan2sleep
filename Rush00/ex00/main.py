'''Main file - includes both Success and Fail cases'''
from checkmate import checkmate

def main():
    print("=== Case 1: King is in check (Expect: Success) ===")
    board1 = """\
....
.K..
....
.Q..\
"""
    checkmate(board1)

if __name__ == "__main__":
    main()
