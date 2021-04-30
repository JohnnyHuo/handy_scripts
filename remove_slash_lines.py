#!/usr/bin/env python

a_file = open("source_file.txt", "r")

lines = a_file.readlines()
a_file.close()

new_file = open("processed_files.txt", "w")
for line in lines:
    if "/" not in line:
        new_file.write(line)

new_file.close()
