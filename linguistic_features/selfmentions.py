"""The script prints the self-mentions and counts their total number per article section."""

import sys
import spacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
# The script below prints the self-mentions and their count in each article introduction.
# To change the section type, simply replace "introductions.txt" with
# "abstracts.txt", or
# "relatedwork.txt", or
# "discussions.txt", or
# "conclusions.txt".
f = open("introductions.txt", "r", encoding="utf-8")
#line_cnt = 0
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            low_case = file_text.lower()
            doc = nlp(low_case)
            Prons = ["we", "our", "us", "I", "my", "mine", "me"]
            self_mentions = []
            for token in doc:
                if token.text == token.text in Prons:
                    self_mentions.append(token.text)
            print(file_name)
            print("Self-mentions found in the section:", self_mentions)
            print("Total number of self-mentions: ", len(self_mentions))

