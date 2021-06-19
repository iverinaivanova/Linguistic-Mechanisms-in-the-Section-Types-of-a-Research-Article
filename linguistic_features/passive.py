"""The script retrieves occurrences of passive voice using spacy's rule-based matching engine.
The rule-based matching engine allows the search and the retrieval of exactly
defined token sequences and phrases such as the passive voice pattern below.
The pattern is adapted from https://gist.github.com/armsp/30c2c1e19a0f1660944303cf079f831a."""

import spacy
from spacy.matcher import Matcher
from collections import Counter
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Opening and reading the raw data with the extracted section types.
# Here it is set to conclusions. To run the script on the rest of the section types, simply replace
# the file name with:
# "abstracts.txt" -- abstracts
# "introductions.txt" -- introductions
# "relatedwork.txt" -- related works
# "discussions.txt" -- discussions

f = open("conclusions.txt", "r", encoding="utf-8")
line_cnt = 0
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            doc = nlp(file_text)
            sents = list(doc.sents)
            all_matches = []
            # Passive Voice Pattern
            passive_rule = [{'DEP':'nsubjpass'},{'DEP':'aux','OP':'*'},{'DEP':'auxpass'},{'TAG':'VBN'}]
            matcher.add('Passive',None,passive_rule)
            matches = matcher(doc)
            print(file_name)
            for match_id, start, end in matches:
                matched_span = doc[start:end]
                # print(matched_span.text)
                all_matches.append(matched_span.text)
            passives_count = len(all_matches)
            print("Passives found in the section: ", all_matches)
            print("Total number of passive constructions: ", passives_count)
