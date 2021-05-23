## Linguistic-Mechanisms-in-the-Sections-of-a-Research-Article
 
### Overview of the repository
The repository contains:

1) a folder with java-based scripts (**sectionsretrieval**) with which 5 section types were retrieved from research articles in the field of Compulational Linguistics available from ACL Anthology Reference Corpus](https://acl-arc.comp.nus.edu.sg/)); 

2) a folder with python-based scripts with which the frequency scores of a set of linguistic features were retrieved. 


### How to run the scripts
**Prerequisites for the _Coreference_ script:**
- To run the section retrieval scripts from the **sectionsretrieval** folder in your IDE, make sure that the subbranch called **Libraries** is not empty (i.e. it contains Stanford CoreNLP libraries that the scripts require to run the CoreNLP annotators). If the Libraries directory is empty, do the following:
1. Download Stanford CoreNLP https://stanfordnlp.github.io/CoreNLP/download.html and unarchive it.
2. Then go back to the **Libraries** subbranch, select it, and right click on it. Then select **Add JAR/Folder**, search for the corenlp package that you've already unarchived and load all libraries from the folder.


**Prerequisites for the python scripts**
- Python 3.8 or later version
- spaCy version  2.2.4
