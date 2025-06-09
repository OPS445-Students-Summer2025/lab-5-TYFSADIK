#!/usr/bin/env python3

def read_file_string(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_file_list(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def append_file_string(filename, string):
    with open(filename, 'a') as f:
        f.write(string)

def write_file_list(filename, list1):
    with open(filename, 'w') as f:
        for item in list1:
            f.write(item + '\n')

def copy_file_add_line_numbers(filename1, filename2):
    with open(filename1, 'r') as f1, open(filename2, 'w') as f2:
        for i, line in enumerate(f1, 1):
            f2.write(f"{i}:{line.strip()}\n")
