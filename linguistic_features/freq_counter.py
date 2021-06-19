# -*- coding: utf-8 -*-
""" The script retrieves the most frequent nouns/verbs/adjectives/adverbs per section type."""

import logging
import spacy
logging.basicConfig(level=logging.DEBUG)

# Set the section type you want to analyze.
FILE_NAME = 'abstracts.txt'
# Set this to the maximum number of files(articles) you want to process.
LIMIT = 8000
# Set this to the part of speech you want to count.
POS = 'VERB'


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
    file_cnt = 1
    for line in lines:
        split = line.strip().split('\t')
        if len(split) > 1:
            # Get an intro.
            an_intro = line[line.index("\t"):].strip()
            # print(an_intro)
            # Pos tag it.
            doc = nlp(an_intro)
            for token in doc:
                tok = token.text
                pos = token.pos_
                lem = token.lemma_
                # Check your specified part-of-speech.
                if pos == POS:
                 lemma_list.append(lem)
            print("Processed file num:", file_cnt)
            file_cnt += 1
            if file_cnt == LIMIT:
                break
    count_frequency(lemma_list)


if __name__ == "__main__":
    main()

