from SPARQLWrapper import SPARQLWrapper, JSON

def query(sparql):
    # Set the SPARQL endpoint URL
    endpoint = SPARQLWrapper("http://wit.istc.cnr.it/geno/sparql")

    # This query allows to get the data representing the training set.
    endpoint.setQuery(sparql)
    endpoint.setReturnFormat(JSON)
    return endpoint.query().convert()
    
    


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

# Finally, we print the stats.
print("# of individuals in the training graph: " + trainingGraphStats)
print("# of individuals in the test graph: " + testGraphStats)
print("# of individuals in the validation graph: " + validationGraphStats)


