## Linguistic-Mechanisms-in-the-Sections-of-a-Research-Article
 
### Overview of the repository
The repository contains a folder with Java-based scripts with which 5 section types from (**src** folder) that parses multiple articles in Compulational Linguistics in xml form (the files can be accessed from the **all_Ks** folder. Source: [ACL Anthology Reference Corpus](https://acl-arc.comp.nus.edu.sg/)), and uses [the Stanford CoreNLP Module](https://stanfordnlp.github.io/CoreNLP/index.html) to output coreference analysis per document (mean number of coreference chains), as well as mean number of tokens, mean sentence length, mean number of self mentions, mean number of NPs, mean number of finite and non-finite clauses embedded in the NP structure.

- Note that the **all_Ks** does not contain the whole corpus.

- The data set with the features and their computed values per text type are available under the **annotations** folder.

### How to run the script
**Things to consider before you run the Java-based scripts:**
- To run the section retrieval scripts from the **sectionsretrieval** folder in your IDE, make sure that the subbranch called **Libraries** is not empty (i.e. it contains Stanford CoreNLP libraries that the scripts require to run the CoreNLP annotators). If the Libraries directory is empty, do the following:
1. Download Stanford CoreNLP https://stanfordnlp.github.io/CoreNLP/download.html and unarchive it.
2. Then go back to the **Libraries** subbranch, select it, and right click on it. Then select **Add JAR/Folder**, search for the corenlp package that you've already unarchived and load all libraries from the folder.
