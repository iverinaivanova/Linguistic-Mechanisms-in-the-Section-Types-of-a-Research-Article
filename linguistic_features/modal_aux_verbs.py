"""The script prints the occurrences of modal auxiliary verbs and counts their number per article section."""
import sys
import spacy
from collections import Counter
nlp = spacy.load("en_core_web_lg")
f = open("abstracts.txt", "r", encoding="utf-8")
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            lower_text = file_text.lower()
            doc = nlp(lower_text)
            modals = ["might", "may", "could", "should", "can", "would", "will", "shall"]
            hedges = []
            for token in doc:
                if token.text == token.text in modals:
                    hedges.append(token.text)
            mod_aux_count = len(hedges)
            print(file_name)
            print("Modal auxiliaries found in the section: ", hedges)
            print("Total number of modal auxiliaries: ", mod_aux_count)