"""The script prints the occurrences of the pattern (I/we + verb + that-compl) per article section and then
prints their total number."""

import spacy
from spacy.matcher import Matcher
from collections import Counter
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Opening and reading the raw data with the extracted section types.
# Here it is set to discussions. To run the script on the rest of the section types, simply replace
# the file name with:
# "abstracts.txt" -- abstracts
# "introductions.txt" -- introductions
# "relatedwork.txt" -- related works
# "conclusions.txt" -- conclusions.
f = open("discussions.txt", "r", encoding="utf-8")
line_cnt = 0
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            lower_case = file_text.lower()
            doc = nlp(lower_case)
            sents = list(doc.sents)
            all_matches = []
            verb_rule1 = [{'DEP': 'nsubj', 'POS': 'PRON', 'TEXT': 'we'},
                         {'POS': 'VERB'},
                         {'LEMMA': 'that', 'POS': 'SCONJ'}]
            verb_rule2 = [{'DEP': 'nsubj', 'POS': 'PRON', 'TEXT': 'i'},
                          {'POS': 'VERB'},
                          {'LEMMA': 'that', 'POS': 'SCONJ'}]
            matcher.add('Verb Rule1', None, verb_rule1)
            matcher.add('Verb Rule2', None, verb_rule2)
            matches = matcher(doc)
            for match_id, start, end in matches:
                matched_span = doc[start:end]
                # print(matched_span.text)
                all_matches.append(matched_span.text)
            vpattern_count = len(all_matches)
            print(file_name)
            print("Verb patterns: ", all_matches)
            print("Total number of verb patterns: ", vpattern_count)
                # Operators and quantifiers
                #  'OP': '!' Negation: match 0 items
                #  'OP': '?' Optional: match 0 or 1 times
                #  'OP': '+' Match 1 or more times
                #  'OP': '*' Match 0 or more times
