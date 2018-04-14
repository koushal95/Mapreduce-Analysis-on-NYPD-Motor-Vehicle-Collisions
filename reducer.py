#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# for each line in mapper output
for line in sys.stdin:
        # remove the whitespaces
        line = line.strip()
        # split the input on tab space and make only one split
        word, count = line.split('\t', 1)
        # try making the count variable as integer
        try:
                count = int(count)
        except ValueError:
                continue
        # if its the same word increment count
        if current_word == word:
                current_count += count
        else:
                # if new word came in and we have seen a word already print that seen word's statistic
                if current_word:
                        print '%s\t%s' % (current_word, current_count)
                # Now the new word becomes the current word
                current_count = count
                current_word = word
# print the last word
if current_word == word:
        print '%s\t%s' % (current_word, current_count)
