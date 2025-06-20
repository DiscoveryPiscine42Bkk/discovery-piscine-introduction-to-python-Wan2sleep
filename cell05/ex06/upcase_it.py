import sys
def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].upper())
    else:
        user_input = input("Please enter a parameter: ").strip()
        if user_input:
            print(user_input.upper())
        else:
            print("none")

if __name__ == "__main__":
    main()