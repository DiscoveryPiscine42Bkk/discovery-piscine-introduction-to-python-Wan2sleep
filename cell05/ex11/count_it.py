import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        user_input = input("Please enter parameters (separate with spaces): ").strip()

        if user_input:
            params = user_input.split()
            print(f"parameters: {len(params)}")
            for param in params:
                print(f"{param}):\n{len(param)}")
        else:
            print("none")
    
    else:
        print(f"parameters: {len(sys.argv) - 1}")
        for param in sys.argv[1:]:
            print(f"{param}):\n{len(param)}")

if __name__ == "__main__":
    main()