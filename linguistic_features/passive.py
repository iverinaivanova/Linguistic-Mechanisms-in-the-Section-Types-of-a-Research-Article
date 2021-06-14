import spacy
from spacy.matcher import Matcher
from collections import Counter
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
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
            passive_rule = [{'DEP':'nsubjpass'},{'DEP':'aux','OP':'*'},{'DEP':'auxpass'},{'TAG':'VBN'}]
            matcher.add('Passive',None,passive_rule)
            matches = matcher(doc)
            print(file_name)
            for match_id, start, end in matches:
                matched_span = doc[start:end]
                print(matched_span.text)
                all_matches.append(matched_span.text)
            print(matches)
            # passives_abstract = open("passive_matches_abstract.txt", "w", encoding="utf-8")
            # passives_concls = open("passive_matches_concls.txt", "a", encoding="utf-8")
            # passives_concls.write(file_name + "\t" + str(all_matches) + "\n")