import sys
def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        user_input = input("Please enter a parameter: ").strip()
        if user_input:
            print(user_input.lower())
        else:
            print("none")

if __name__ == "__main__":
    main()