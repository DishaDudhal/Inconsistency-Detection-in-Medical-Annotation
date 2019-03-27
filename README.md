# Inconsistency Detection in Medical Annotation
Inconsistency Detection in Medical Annotation using UMLS Dictionary lookup based Approach.
UMLS or Unified Medical Language System is a set of files that brings together many health and biomedical vocabularies and standards to enable interoperability between computer systems.
# How to Approach?
The following problem can be solved either by Machine Learning models or Dictionary lookup.
The method described in this repository is the Dictionary lookup based Approach, in which we dive into the UMLS in order to find syntactical similarity. We have to find the words or word phrases that are differently annotated in the whole dataset and present them in a web application. The web application is developed on Django framework.
# Dependencies
- UMLS
- QuickUMLS API
- Django Framework
# About Dataset
The are 'n' number of rows and the first column of each row contains a normal sentence or statement. The annotated texts in each sentence is stored in separate columns, so a particular sentence has no fixed number of columns.
The entities having a relation comes together in a single column.
The dataset is in a .tsv file (tab separated values). The dataset is not Available due to Privacy Agreements.
