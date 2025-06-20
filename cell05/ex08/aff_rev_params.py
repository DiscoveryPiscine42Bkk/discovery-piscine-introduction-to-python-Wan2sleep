import sys
def main():
    if len(sys.argv) > 1:
        params = [arg for arg in sys.argv[1:] if arg.strip() != ""]

    else:
        user_input = input("Please enter parameters (separate with spaces): ").strip()
        if user_input:
            params = user_input.split()
        else:
            params = []

    if len(params) < 2:
        print("none")
    else:
        for arg in reversed(params):
            print(arg)

if __name__ == "__main__":
    main()