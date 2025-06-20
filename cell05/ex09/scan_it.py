import sys
import re

def main():
    if len(sys.argv) == 3:
        keyword = sys.argv[1]
        text = sys.argv[2]
    else:
        keyword = input("Enter the keyword: ").strip()
        text = input("Enter the text: ").strip()

    matches = re.findall(re.escape(keyword), text)

    if matches:
        print(len(matches))
    else:
        print("none")

if __name__ == "__main__":
    main()