"""The script gets all lemmas of content words and stores them in a list.
Then it iterates over the list and finds duplicates (repeated words)
as a measure for lexical cohesion. It prints the repeated word and its count (lexical chain).
It prints the total number of lexical chains. Finally, it prints the sum of all counts."""

import spacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
f = open("relatedwork.txt", "r", encoding="utf-8")
#line_cnt = 0
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            low_case = file_text.lower()
            doc = nlp(low_case)
            lemmas = []
            print(file_name)
            for token in doc:
                if token.is_alpha and token.pos_ == "NOUN" or token.pos_ == "VERB" or token.pos_ == "ADJ" or token.pos_ == "ADV":
                    lemmas.append(token.lemma_)
            def getDuplicatesfromList(listOfItems):
                dictOfElems = dict()
                for elem in listOfItems:
                    if elem in dictOfElems:
                        dictOfElems[elem] += 1
                    else:
                        dictOfElems[elem] = 1
                dictOfElems = {key:value for key, value in dictOfElems.items() if value > 1}
                return dictOfElems
            dictOfElems = getDuplicatesfromList(lemmas)
            for key,value in dictOfElems.items():
                result = key , ':', value
                # print(key , ':', value)
            print("Lexical chains: ", dictOfElems)
            count_lex_chains = len(dictOfElems)
            print("Number of lexical chains: ", count_lex_chains)
            my_values = dictOfElems.values()
            total = sum(my_values)
            print("Sum of all counts: ", total)
