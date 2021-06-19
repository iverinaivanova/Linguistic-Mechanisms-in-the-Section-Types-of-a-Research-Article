"""The script processes the extracted verb patterns found in the article sections
(pronoun+verb+that-clause) and prints the most frequent verbs per section type."""

import logging
import spacy
logging.basicConfig(level=logging.DEBUG)
from spacy.matcher import Matcher

# Setting the file containing the extracted verb patterns (pronoun+verb+that-clause).
# Here it is set to the verb patterns found in the conclusion sections.
# To get the most frequent verbs from the rest of the sections, simply replace the FILE_NAME with :
# 'vpatternText_abstracts.txt' -- abstracts,
# 'vpatternText_intros.txt' -- introductions,
# 'vpatternText_rworks.txt' -- related works,
# 'vpatternText_discs.txt' -- conclusions.
FILE_NAME = 'vpatternText_concls.txt'

# Set this to the maximum number of files(articles) you want to process.
LIMIT = 8000

# Defining a frequency counter function


def count_frequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for k in sorted(freq, key=freq.get, reverse=True):
        print(k, freq[k])


def main():
    logging.info('Running freq_counter.py...')
    # Install with:
    # python -m spacy download en_core_web_sm
    nlp = spacy.load("en_core_web_sm")
    intros = open(FILE_NAME, 'r', encoding="utf-8")
    lines = intros.readlines()
    lemma_list = []
    all_matches = []
    file_cnt = 1
    for line in lines:
        split = line.strip().split('\t')
        if len(split) > 1:
            # Get an intro.
            an_intro = line[line.index("\t"):].strip()
            # print(an_intro)
            # Pos tag it.
            doc = nlp(an_intro)
            matcher = Matcher(nlp.vocab)
            sents = list(doc.sents)
            lexv_rule = [{'POS': 'VERB'}]
            matcher.add('LexVerb', None, lexv_rule)
            matches = matcher(doc)
            for match_id, start, end in matches:
                matched_span = doc[start:end]
                # print(matched_span.text)
                all_matches.append(matched_span.text)
            # print("Processed file num:", file_cnt)
            file_cnt += 1
            if file_cnt == LIMIT:
                break
    count_frequency(all_matches)




if __name__ == "__main__":
    main()