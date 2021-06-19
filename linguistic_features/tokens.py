"""The script prints the total number of tokens per article section."""

import sys

"""The script below prints the number of tokens of abstracts per article.
To change the section type, simply replace "abstracts.txt" with
"introductions.txt", or
"relatedwork.txt", or
"discussions.txt", or
"conclusions.txt". """

f = open("abstracts.txt", "r", encoding="utf-8")
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            print(file_name)
            num_tokens = len(file_text.split(' '))
            if (num_tokens) > 0:
                print("Number of tokens:", num_tokens)
            else:
                print(0)
