import sys

def main():
    if len(sys.argv) != 2:
        param = input("Enter the parameter: ").strip()

    else:
         param = sys.argv[1]
    user_input = input("What was the parameter? ").strip()

    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()