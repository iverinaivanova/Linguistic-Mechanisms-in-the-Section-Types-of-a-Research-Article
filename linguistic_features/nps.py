# This script prints all NP occurrences and their total number for each text.
# It also prints all NPs in which the noun head takes dependents and counts their number.

import sys
import spacy

# Loading the statistical model and storing it in the nlp object.
# The statistical model enables spacy to make predictions about
# the linguistic attributes of the tokens in context.
nlp = spacy.load("en_core_web_sm")

# Opening the raw data with the extracted section types
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

            # Initializing an empty list to which all NP occurrences per text will be appended.
            NPs = []
    
            # An empty list to which all NPs containing adjective dependents will be appended.
            ADJ_DEP = []
            # An empty list to which all NPs containing noun dependents will be appended.
            NOUN_DEP = []
            # An empty list to which all NPs containing PP dependents will be appended.
            PREP_DEP = []

            # Iterate over each constituent in the document and append to the empty list
            # the NP (noun constituents). Then count the total number of NPs in each list.
            for chunk in doc.noun_chunks:
                NPs.append(chunk)
            print("NPs: ", NPs)
            for chunk in NPs:
                for token in chunk:
                    for child in token.children:
                        if child.pos_ == "ADJ":
                            ADJ_DEP.append(chunk)
                        elif child.pos_ == "NOUN":
                            NOUN_DEP.append(chunk)
                        elif child.pos_ == "ADP":
                            PREP_DEP.append(chunk)
            print("File name ", file_name)
            print("NPs containing ADJ:", ADJ_DEP)
            print("Total # NPs containing ADJs: ", len(ADJ_DEP))
            print("NPs containing NOUN_DEP:", NOUN_DEP)
            print("Total # NPs containing NOUN_DEP: ", len(NOUN_DEP))
            print("NPs containing PPs: ", PREP_DEP)
            print("Total # NPs containing PPs: ", len(PREP_DEP))
