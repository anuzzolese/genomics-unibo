from io import StringIO
from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template, request
import pandas as pd
from sklearn.naive_bayes import GaussianNB

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

@app.route("/")
def home():
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?split ?sequence ?class ?gene
        FROM <http://wit.istc.cnr.it/geno/validation>
        WHERE {
            ?split <http://wit.istc.cnr.it/geno/sequence> ?sequence
        }
        """
    results = query(sparql)
    
    individuals = []
    for result in results["results"]["bindings"]:
        
        sequence = ""
        for c in result["sequence"]["value"]:
            value = ord(c)
            if len(sequence) > 0:
                sequence += ","
            
            sequence += str(value)
            
        ind = result["split"]["value"]
        individuals.append(ind)
        
    return render_template('template.html', validationSet=individuals)

@app.route("/classify", methods=['POST'])
def classify():
    ind = request.form['individual']
    
    sparql = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?split ?sequence ?class ?gene
        FROM <http://wit.istc.cnr.it/geno/validation>
        WHERE {
            <""" + ind + """> <http://wit.istc.cnr.it/geno/sequence> ?sequence
        }
        """
    results = query(sparql)
    sequence = []
    for result in results["results"]["bindings"]:
        for c in result["sequence"]["value"]:
            # We append the integer representationg of the sequence element.
            sequence.append(ord(c))
        
    # Here we compute the prediction
    predictions = classifier.predict([sequence])
    
    return render_template('classification.html', individual=ind, predictions=predictions)


trainingSet = getTrainingSet()
X_train, y_train = trainingSet.iloc[:, :-1], trainingSet.iloc[:, -1]

classifier.fit(X_train, y_train)

if __name__ == '__main__':
    app.run(debug=True)