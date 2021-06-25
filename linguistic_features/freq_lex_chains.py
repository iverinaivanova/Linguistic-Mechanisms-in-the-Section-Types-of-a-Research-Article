"""The script prints the most frequent repeated word from the lexical chains per section type"""

import logging
import spacy
logging.basicConfig(level=logging.DEBUG)


# Setting the file containing the lexical chains per section type.
# Here it is set to the lexical chains found in the conclusion sections.
# To get the most frequent repeated word from the rest of the sections, simply replace the FILE_NAME with :
# 'lex_chains_abstracts.txt' -- abstracts,
# 'lex_chains_intros.txt' -- introductions,
# 'lex_chains_rworks.txt' -- related works,
# 'lex_chains_discs.txt' -- conclusions.
# To run the script, make sure that you place the .txt files in the same directory in which the script is stored or 
# add the full path to the files: "..supplements/vpattern/lex_chains_concls.txt".

FILE_NAME = 'lex_chains_concls.txt'
# Set this to the maximum number of files you want to process.
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
    file_cnt = 1
    for line in lines:
        split = line.strip().split('\t')
        if len(split) > 1:
            # Get an intro.
            an_intro = line[line.index("\t"):].strip()
            doc = nlp(an_intro)
            for token in doc:
                if token.is_alpha and token.pos_ == "NOUN" or token.pos_ == "VERB" or token.pos_ == "ADJ" or token.pos_ == "ADV":
                    lemma_list.append(token.lemma_)
                # Check your specified part-of-speech.
            # print("Processed file num:", file_cnt)
            file_cnt += 1
            if file_cnt == LIMIT:
                break
    count_frequency(lemma_list)


if __name__ == "__main__":
    main()
