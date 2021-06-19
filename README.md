## Linguistic-Mechanisms-in-the-Sections-of-a-Research-Article
 
### Overview of the repository


1) an *xml* folder which contains example research articles in the field of Compulational Linguistics available from [ACL Anthology Reference Corpus](https://www.aclweb.org/anthology/); 

2) a folder with java-based scripts (*sectionsretrieval*) which retrieve 5 section types from the research articles 

3) a folder with scripts (*linguistic_features*) which retrieve the linguistic features and their frequency scores 

4) *raw texts* which contains all detected and extracted sections from each analysed research article

5) a *dataset* folder which contains all computed values for each feature per section type

6) a *supplements* folder which contains lists of extracted lexical chains, passive constructions, and examples of verbs which take 2 arguments (1st p. sg/pl subject and that-complement clause). 


### How to run the scripts
- When you download the java package and load it in your IDE, to run the *Coreference.java* script, which retrieves the total number of coreference chains per text, make sure that the subbranch called **Libraries** is not empty (i.e. it contains Stanford CoreNLP libraries that the script requires to run the CoreNLP annotators). If the Libraries directory is empty, do the following:
1. Download Stanford CoreNLP https://stanfordnlp.github.io/CoreNLP/download.html and unarchive it.
2. Then go back to the **Libraries** subbranch, select it, and right click on it. Then select **Add JAR/Folder**, search for the corenlp package that you've already unarchived and load all libraries from the folder.


**Prerequisites for the python scripts**
- Python 3.8 or later version
- SpaCy version  2.2.4
- When you load the scripts in the IDE, before you run them, make sure that you have configured the Python Interpreter. To do so:
  - go to File > Settings > Project: Users > Python Interpreter > Project interpreter > Expand the list of available interpreters > Select the target interpreter
- To isntall spacy, you can use the following command: `pip install spacy`
- To dowmload a statistical model, you can use the following command: `python -m spacy download en_core_web_sm`. It downloads the small statistical model for English.
