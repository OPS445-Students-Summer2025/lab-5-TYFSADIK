#!/usr/bin/env python3

def read_file_string(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_file_list(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]
