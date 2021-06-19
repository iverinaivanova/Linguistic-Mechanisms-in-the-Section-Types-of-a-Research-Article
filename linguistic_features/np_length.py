"""The script prints the token-based NP length and the sum of all NP lengths for each article section."""

import sys
# Importing the library for NLP
import spacy

# Loading the statistical model and storing it in the nlp object.
# The statistical model enables spacy to make predictions about
# the linguistic attributes of the tokens in context.
nlp = spacy.load("en_core_web_sm")

# Opening and reading the raw data with the extracted section types.
# Here it is set to abstracts. To run the script on the rest of the section types, simply replace
# the file name with:
# "introductions.txt" -- introductions
# "relatedwork.txt" -- related works
# "discussions.txt" -- discussions
# "conclusions.txt" -- conclusions.
f = open("abstracts.txt", "r", encoding="utf-8")

# Accessing the textual content of the tab-separated file and storing it in the "file_text" variable
for line in f:
    if len(line) > 0:
        items = line.split("	")
        if len(items) > 1:
            file_name = items[0]
            file_text = items[1]

            # Converting the text to lower case
            low_case = file_text.lower()

            # Calling the nlp object on the texts to be processed. The nlp object contains the
            # processing pipeline and the language-specific rules for tokenization.
            doc = nlp(low_case)

            # Initializing an empty list to which all NP occurrences per  will be appended.
            NPs = []

            # Initializing an empty list to which the lengths of the individual NP chunks
            # per article section will be appended.
            NP_lengths= []

            # Iterate over each constituent in the document and append to the empty list
            # the NP (noun constituents). Then count the total number of NPs in each list.
            for chunk in doc.noun_chunks:
                NPs.append(chunk)
            for chunk in NPs:
                for token in chunk:
                    chunk_length = len(chunk)
                NP_lengths.append(chunk_length)

            print("File name ", file_name)
            # print("NPs: ", NPs)
            print("NP lengths: ", NP_lengths)
            print("Sum of the NP lengths: ", sum(NP_lengths))
