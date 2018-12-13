from SPARQLWrapper import SPARQLWrapper, JSON
from io import StringIO
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import itertools

def query(sparql):
    # Set the SPARQL endpoint URL
    endpoint = SPARQLWrapper("http://wit.istc.cnr.it/geno/sparql")

    # This query allows to get the data representing the training set.
    endpoint.setQuery(sparql)
    endpoint.setReturnFormat(JSON)
    results = endpoint.query().convert()
    
    # Convert the result set into an in-memory CSV dataset 
    data = ""
    for result in results["results"]["bindings"]:
        data += result["split"]["value"] 
    
        for c in result["sequence"]["value"]:
            value = ord(c)
            data += "," + str(value)
        if result.has_key("class"): 
            data += "," + result["class"]["value"] + "\n"
    
    # Generate a Pandas data frame from the in-memory CSV so that it can be used by scikit-learn and return it.
    return pd.read_csv(StringIO(data), sep=",", index_col=0)

def plotMatrix(cm, classes):
        cmap=plt.cm.Blues
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title('Confusion matrix')
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.tight_layout()
        
        # The line below saves the confution matrix on a PNG file named out.png.
        plt.savefig("out.png", dpi=None, facecolor='w', edgecolor='w',
                    orientation='portrait', papertype=None, format=None,
                    transparent=False, bbox_inches='tight', pad_inches=0.3,
                    frameon=None)
        
        # The line belows shows the confution matrix on screen.
        plt.show()
    

# Query for getting the data representing the training set.
sparql = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?split ?sequence ?class ?gene
    FROM <http://wit.istc.cnr.it/geno/training>
    WHERE {
        ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence ;
            <http://wit.istc.cnr.it/geno/classification> ?class
    }
    """
trainingSet = query(sparql)


# Query for getting the data representing the test set.
sparql = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?split ?sequence ?class ?gene
    FROM <http://wit.istc.cnr.it/geno/test>
    WHERE {
        ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence ;
            <http://wit.istc.cnr.it/geno/classification> ?class
    }
    """
testSet = query(sparql)

# Query for getting the data representing the validation set.
sparql = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?split ?sequence ?class ?gene
    FROM <http://wit.istc.cnr.it/geno/validation>
    WHERE {
        ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence
    }
    """
validationSet = query(sparql)


X_train, y_train = trainingSet.iloc[:, :-1], trainingSet.iloc[:, -1]
X_test, y_test = testSet.iloc[:, :-1], testSet.iloc[:, -1]

# We use the Gaussian Naive Bayes as classifier.
classifier = GaussianNB()
classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)

precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')


print ("Precision %(prec)f" % {"prec": precision})
print ("Recall %(rec)f" % {"rec": recall})
print ("F1-measure %(fmeas)f" % {"fmeas": f1})

confusionMatrix = confusion_matrix(y_test, predictions)

plotMatrix(confusionMatrix, ["ie", "ei", "n"])