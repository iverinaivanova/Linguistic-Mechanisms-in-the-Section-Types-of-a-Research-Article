"""The script retrieves explicit connectives marking temporal, comparison, contingency, and expansion relations
and prints the total number of these connectives per article section."""

import sys
import spacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

# The script below retrieves the connectives from each article abstract
# and prints their total number.
# To change the section type, simply replace "abstracts.txt" with
# "introductions.txt" -- for introductions,
# "relatedwork.txt" -- for related works,
# "discussions.txt" -- for discussions,
# "conclusions.txt" -- for conclusions.
f = open("abstracts.txt", "r", encoding="utf-8")
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]
            low_case = file_text.lower()
            doc = nlp(low_case)
            temporal = {"after", "afterwards", "before",
                        "earlier", "later", "meanwhile",
                        "next", "previously", "simultaneously", "thereafter",
                        "till", "until", "ultimately"
                        }
            comparison = {"although", "but", "conversely", "however",
                          "instead", "nevertheless", "nonetheless", "rather",
                          "though", "whereas", "yet", "regardless", "despite", "though"
                          }
            contingency = {"as", "because", "consequently", "hence", "if",
                           "thereby", "therefore", "thus", "so", "indeed", "accordingly"}
            expansion = {"also", "alternatively", "besides", "else", "except",
                         "finally", "further", "furthermore", "likewise",
                         "moreover", "neither", "nor", "or", "otherwise", "overall", "plus",
                         "separately", "similarly", "specifically",
                         "especially", "first", "second", "firstly", "secondly"}

            temporal_relations = []
            comparison_relations = []
            contingency_relations = []
            expansion_relations = []
            for token in doc:
                if token.text == token.text in temporal:
                    temporal_relations.append(token.text)
                elif token.text == token.text in comparison:
                    comparison_relations.append(token.text)
                elif token.text == token.text in contingency:
                    contingency_relations.append(token.text)
                elif token.text == token.text in comparison:
                    expansion_relations.append(token.text)
            print(file_name)
            print("Temporal connectives found in the section:", temporal_relations)
            print("Total number of connectives:", len(temporal_relations))
            print("Comparison connectives found in the section:", comparison_relations)
            print("Total number of connectives:", len(comparison_relations))
            print("Contingency connectives found in the section:", contingency_relations)
            print("Total number of connectives:", len(contingency_relations))
            print("Expansion connectives found in the section:", expansion_relations)
            print("Total number of connectives:", len(expansion_relations))