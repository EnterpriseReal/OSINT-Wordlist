#! /usr/bin/env python3

# I am the best!

import argparse
from itertools import combinations


parser = argparse.ArgumentParser()
parser.add_argument('--infile', type=str, required=True, help='The file to be parsed')
parser.add_argument('--outfile', type=str, required=True, help='Outfile for the program')
parser.add_argument('--depth', type=int, required=False, help='Optional setting, default 2')

args = parser.parse_args()

new_list = list()
all_words = list()

with open(args.infile, 'r') as i:
    words = [word.strip() for word in i.readlines()]

for word in words:
    all_words.append(word.capitalize())
    all_words.append(word.upper())


for n in range(len(all_words) + 1):
    new_list += list(combinations(all_words, n))

with open(args.outfile, 'a') as out:
    for tup in new_list:
        if args.depth:
            if len(tup) in range(1, args.depth + 1):
                new_str = ''.join(tup)
                out.write(new_str + '\n')
        else:
            if len(tup) == 2:
                new_str = ''.join(tup)
                out.write(new_str + '\n')
