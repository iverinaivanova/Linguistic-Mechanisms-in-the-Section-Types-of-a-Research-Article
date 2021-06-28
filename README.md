## Linguistic-Mechanisms-in-the-Sections-of-a-Research-Article
 
### Overview of the repository


1) a folder with java scripts (*src/sectionsretrieval*) which retrieve 5 section types from the research articles 

2) a folder with python scripts (*linguistic_features*) which retrieve the linguistic features and their frequency scores 

3) *raw texts* which contains all detected and extracted sections from each analysed research article

4) a *dataset* folder which contains all computed values for each feature per section type

5) a *supplements* folder which contains lists of extracted lexical chains, passive constructions, and examples of verbs which take 2 arguments (1st p. sg/pl subject and that-complement clause). 

6) a folder with Mutual Information (MI) scores 

7) an *all_xmls* folder with example xml files from the corpus.


### ACL Anthology Corpus 
Source: ACL Anthology Reference Corpus: https://www.aclweb.org/anthology/ (Originally downloaded from the repo from: https://acl-arc.comp.nus.edu.sg/). The folder *all_xmls*
contains example xml files to give the users an idea of the corpus format.

### How to run the scripts
- When you download the java package and load it in your IDE, to run the *Coreference.java* script, which retrieves the total number of coreference chains per text, make sure that the subbranch called **Libraries** is not empty (i.e. it contains Stanford CoreNLP libraries that the script requires to run the CoreNLP annotators). If the Libraries directory is empty, do the following:
1. Download Stanford CoreNLP https://stanfordnlp.github.io/CoreNLP/download.html and unarchive it.
2. Then go back to the **Libraries** subbranch, select it, and right click on it. Then select **Add JAR/Folder**, search for the corenlp package that you've already unarchived and load all libraries from the folder.


**Prerequisites for the python scripts**
- Python 3.8 or later version
- SpaCy version  2.2.4
- When you load the scripts in the IDE, before you run them, make sure that you have configured the Python Interpreter. To do so:
  - go to File > Settings > Project: Users > Python Interpreter > Project interpreter > Expand the list of available interpreters > Select the target interpreter
- To install spacy, you can use the following command: `pip install spacy`
- To download a statistical model, you can use the following command: `python -m spacy download en_core_web_sm`. It downloads the small statistical model for English.
