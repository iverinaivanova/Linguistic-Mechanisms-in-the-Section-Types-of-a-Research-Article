"""The script retrieves the occurrences of nouns taking a past participle (VBN) dependent using spacy's
rule-based matching engine and then counts their number per article section.
The rule-based matching engine allows the search and the retrieval of exactly
defined token sequences and phrases such as the passive voice pattern below."""

import spacy

# Importing the rule-based matching engine
from spacy.matcher import Matcher

from collections import Counter
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
# Opening and reading the raw data with the extracted section types.
# Here it is set to abstracts. To run the script on the rest of the section types, simply replace
# the file name with:
# "introductions.txt" -- introductions
# "relatedwork.txt" -- related works
# "discussions.txt" -- discussions
# "conclusions.txt" -- conclusions.
f = open("abstracts.txt", "r", encoding="utf-8")
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
            np_rule = [
                # {'POS': 'DET', 'OP': '*'},
                # {'POS':'ADJ', 'OP': '*'},
                {'POS': 'NOUN'},

                {'TAG': 'VBN', 'OP': '+'}
            ]
            matcher.add('NP Rule', None, np_rule)
            matches = matcher(doc)
            print(file_name)
            for match_id, start, end in matches:
                matched_span = doc[start:end]
                # print(matched_span.text)
                all_matches.append(matched_span.text)
            pastpart_mod_count = len(all_matches)
            print("Nouns taking a VBN dependent: ", all_matches)
            print("Total number of NPs containing a VBN: ", pastpart_mod_count)

                # Operators and quantifiers
                #  'OP': '!' Negation: match 0 items
                #  'OP': '?' Optional: match 0 or 1 times
                #  'OP': '+' Match 1 or more times
                #  'OP': '*' Match 0 or more times
