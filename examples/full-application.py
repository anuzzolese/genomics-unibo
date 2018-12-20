from io import StringIO
from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template, request
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import itertools, os

# The app is available on port 5000 on your Web browser, i.e. http://localhost:5000
app = Flask(__name__)

# We use the Gaussian Naive Bayes as classifier.
classifier = GaussianNB()

def query(sparql):
    # Set the SPARQL endpoint URL
    endpoint = SPARQLWrapper("http://wit.istc.cnr.it/geno/sparql")

    # This query allows to get the data representing the training set.
    endpoint.setQuery(sparql)
    endpoint.setReturnFormat(JSON)
    return endpoint.query().convert()

def computeStats():
    # We retrieve the number of individuals from training graph.
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT (COUNT(DISTINCT ?split) AS ?inds)
        FROM <http://wit.istc.cnr.it/geno/training>
        WHERE {
            ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence
        }
    """
    results = query(sparql)
    trainingGraphStats = results["results"]["bindings"][0]["inds"]["value"]
    
    # Then, we retrieve the number of individuals from test graph.
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT (COUNT(DISTINCT ?split) AS ?inds)
        FROM <http://wit.istc.cnr.it/geno/test>
        WHERE {
            ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence
        }
        """
    results = query(sparql)
    testGraphStats = results["results"]["bindings"][0]["inds"]["value"]
    
    # Then, we retrieve the number of individuals from validation graph.
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT (COUNT(DISTINCT ?split) AS ?inds)
        FROM <http://wit.istc.cnr.it/geno/validation>
        WHERE {
            ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence
        }
        """
    results = query(sparql)
    validationGraphStats = results["results"]["bindings"][0]["inds"]["value"]
    
    return {"trainingGraphStats": trainingGraphStats,
            "testGraphStats": testGraphStats,
            "validationGraphStats": validationGraphStats}
    
def computeMetrics(classifier):
    training = getTrainingSet()
    test = getTestSet()
    
    X_train, y_train = training.iloc[:, :-1], training.iloc[:, -1]
    X_test, y_test = test.iloc[:, :-1], test.iloc[:, -1]

    # We train the classifier
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)

    precision = precision_score(y_test, predictions, average='weighted')
    recall = recall_score(y_test, predictions, average='weighted')
    f1 = f1_score(y_test, predictions, average='weighted')
    
    cm = confusion_matrix(y_test, predictions)
    
    confusion_matrix_image = saveConfusionMatrix(cm, ["ie", "ei", "n"])

    
    
    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": confusion_matrix_image
        }
    
def saveConfusionMatrix(cm, classes):
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
    
    fileName = "static/confusion-matrix.png"
    
    # The line below saves the confution matrix on a PNG file named out.png.
    plt.savefig(fileName, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches='tight', pad_inches=0.3,
                frameon=None)
    
    return fileName

def rdfjson2pandas(json_results):
    data = ""
    for result in json_results["results"]["bindings"]:
        data += result["split"]["value"] 
    
        for c in result["sequence"]["value"]:
            value = ord(c)
            data += "," + str(value)
        if result.has_key("class"): 
            data += "," + result["class"]["value"] + "\n"
    
    # Generate a Pandas data frame from the in-memory CSV so that it can be used by scikit-learn and return it.
    return pd.read_csv(StringIO(data), sep=",", index_col=0)

def getTrainingSet():
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?split ?sequence ?class ?gene
        FROM <http://wit.istc.cnr.it/geno/training>
        WHERE {
            ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence ;
                <http://wit.istc.cnr.it/geno/classification> ?class
        }
        """
    results = query(sparql)
    
    return rdfjson2pandas(results)

def getTestSet():
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?split ?sequence ?class ?gene
        FROM <http://wit.istc.cnr.it/geno/test>
        WHERE {
            ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence ;
                <http://wit.istc.cnr.it/geno/classification> ?class
        }
        """
    results = query(sparql)
    
    return rdfjson2pandas(results)

def getValidationSet():
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?split ?sequence ?class ?gene
        FROM <http://wit.istc.cnr.it/geno/validation>
        WHERE {
            ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence
        }
        """
    return rdfjson2pandas(results)

def classifyTestExamples(classifier):
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?example ?sequence
        FROM <http://wit.istc.cnr.it/geno/validation>
        WHERE {
            ?example <http://wit.istc.cnr.it/geno/sequence> ?sequence
        }
        """
    results = query(sparql)
    
    classifications = []
    
    for result in results["results"]["bindings"]:
        sequence = []
        example = result["example"]["value"]
        for c in result["sequence"]["value"]:
            # We append the integer representationg of the sequence element.
            sequence.append(ord(c))
            
        # Here we compute the prediction
        predictions = classifier.predict([sequence])
        
        prediction = {
            "id": example,
            "prediction": predictions[0]
        }
        
        classifications.append(prediction)
    
    
    return classifications


@app.route("/")
def webapp():
    
        
    return render_template('allInOne.html', stats=stats, metrics=metrics, predictions=tests)

if __name__ == '__main__':
    classifier = GaussianNB()
    
    if not os.path.exists("static"):
        os.mkdir("static")
    stats = computeStats()
    metrics = computeMetrics(classifier)
    tests = classifyTestExamples(classifier)
    app.run(debug=True)