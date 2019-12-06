# Software Applications @Genomics-UniBO

This project is associated with the Software Application course at the Genomics degree of the University of Bologna.  

The project contains some example snippets of code that can be used for implementing the software application for the student projects.

The snippets must be reengineered and refactored in order to follow the software specification produced by each student group and formalised in the project document.

The snippets are available in the folder labelled 'examples'. Namely:

 - examples/machine-learning.py provides example about how to use [RDFLib](https://github.com/RDFLib/rdflib) and [SPARQLWrapper](https://rdflib.github.io/sparqlwrapper/) in order to gather data from a remote SPARQL endpoint. Namely the SPARQL endpoint is the [GENO](http://wit.istc.cnr.it/sparql) linked open dataset. Gathered data are then pre-processed with [pandas](https://pandas.pydata.org/). Accordingly, the script exemplifies about how to use [scikit-learn](https://scikit-learn.org/stable/) for training a multi-class classifier to predict splice junctions are points on a DNA sequence in terms of exon-intron boundary, intron-exon boundary, and neither (i.e. unknown);
 - examples/user-interface.py implements a simple Web user interface (UI) that provides a Web form. The UI is implemented by using [Flask](http://flask.pocoo.org/) as template engine. The Web form allows a user to select a specific entry form the validation graph of the GENO dataset and return the classification of such an entry with respect to classes exon-intron boundary, intron-exon boundary, and neither (i.e. unknown). The templates are available in the folder examples/tempates, which is used by Flask as default repository of templates. 
