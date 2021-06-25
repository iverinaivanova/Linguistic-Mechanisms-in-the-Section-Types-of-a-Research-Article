"""The script processes all extracted past participle (VBN) from
the passive voice constructions and retrieves the most frequent VBNs per section type."""

import logging
import spacy
logging.basicConfig(level=logging.DEBUG)
from spacy.matcher import Matcher

# Setting the file containing the passive_voice matches per section type.
# Here it is set to the passive voice matches found in the conclusion sections.
# To get the most frequent VBNs from the rest of the sections, simply replace the FILE_NAME with :
# 'passive_matches_abstract.txt' -- abstracts,
# 'passive_matches_intros.txt' -- introductions,
# 'passive_matches_rworks.txt' -- related works,
# 'passive_matches_discs.txt' -- discussions.
# To run the script, make sure that you place the .txt files in the same directory in which the script is stored or 
# add the full path to the files: "..supplements/passives/passive_matches_concls.txt".

FILE_NAME = 'passive_matches_concls.txt'

# Set this to the maximum number of files you want to process.
LIMIT = 8000

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
            passive_rule = [{'TAG': 'VBN'}]
            matcher.add('Passive', None, passive_rule)
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
