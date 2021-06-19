"""This script retrieves the content POS (nouns, verbs, adjectives, adverbs) found in the article sections
and prints their total number."""

import spacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
f = open("abstracts.txt", "r", encoding="utf-8")
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            low_case = file_text.lower()
            doc = nlp(low_case)
            nouns = []
            verbs = []
            adjectives = []
            adverbs = []
            for token in doc:
                if token.pos_=="NOUN":
                    nouns.append(token.text)
                elif token.pos_ == "VERB":
                    verbs.append(token.text)
                elif token.pos_ == "ADJ":
                    adjectives.append(token.text)
                elif token.pos_ == "ADV":
                    adverbs.append(token.text)
            print(file_name)
            print("Nouns: ", nouns)
            print("Total number of nouns: ", len(nouns))
            print("Verbs: ", verbs)
            print("Total number of verbs: ", len(verbs))
            print("Adjectives: ", adjectives)
            print("Total number of adjectives: ", len(adjectives))
            print("Adverbs: ", adverbs)
            print("Total number of adverbs: ", len(adverbs))
