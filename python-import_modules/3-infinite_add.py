#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Exclude the script name
    result = 0

    for arg in argv:
        result += int(arg)

    print(result)
