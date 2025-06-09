#!/usr/bin/env python3

def add(a, b):
    try:
        return int(a) + int(b)
    except Exception:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except Exception:
        return 'error: could not read file'

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: ./lab5c.py <command> [arguments]")
        return

    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 4:
            print("error: add requires 2 arguments")
        else:
            result = add(sys.argv[2], sys.argv[3])
            print(result)
    elif command == "read_file":
        if len(sys.argv) < 3:
            print("error: read_file requires 1 argument")
        else:
            result = read_file(sys.argv[2])
            print(result)
    else:
        print("error: unknown command")

if __name__ == "__main__":
    main()
