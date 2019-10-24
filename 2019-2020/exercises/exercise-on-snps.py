import csv
from abc import ABC, abstractclassmethod

class AlleleVariation(ABC):
    
    @abstractclassmethod
    def isTransition(self):
        pass
    
    @abstractclassmethod
    def isTransversion(self):
        pass
        

class SNP(AlleleVariation):
    
    def __init__(self, refBase, altBase, snpId, snpPosition, chromosomeName):
        #the information in input should be store
        # as private attribute of class's individuals
        self.__refBase = refBase
        self.__altBase = altBase
        self.__snpId = snpId
        self.__snpPosition = snpPosition
        self.__chromosomeName = chromosomeName
    
    # A transition is any combination of 
    # A/G, G/A, C/T, or T/C
    def isTransition(self):
        if self.__refBase != self.__altBase:
            if self.__refBase == "A" and self.__altBase == "G":
                return True
            elif self.__refBase == "G" and self.__altBase == "A":
                return True
            elif self.__refBase == "C" and self.__altBase == "T":
                return True
            elif self.__refBase == "T" and self.__altBase == "C":
                return True
            else: 
                return False
        else:
            return False
        
    # A transversion is any case that is not a transition
    def isTransversion(self):
        return not self.isTransition()

#Implement a Chromosome class that provides four methods: 
# - count_transitions(), which returns the number of transition SNPs
# - count_transversions(), which returns the number of transversion SNPs
# - addSNP(), which add a SNP object into the array of SNPs associated to the current Chromosome
# - getName, which returns the string representing the name of the Chromosome
class Chromosome:
    
    def __init__(self, name):
        self.__name = name
        self.__snps = []
    
    def count_transitions(self):
        transitions = 0
        for snp in self.__snps:
            if snp.isTransition:
                transitions = transitions + 1
        
        return transitions
    
    def count_transversions(self):
        pass
    
    def addSNP(self, snp):
        self.__snps.append(snp)
    
    def getName(self):
        return self.__name
    
        
with open('trio.sample.vcf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    
    chromosomeDict = dict()
    for row in csv_reader:
        chromosomeName = row[0]
        snpPosition = row[1]
        snpId = row[2]
        refAllele = row[3]
        altAllele = row[4]
        
        chromosome = chromosomeDict.get(chromosomeName, None)
        if chromosome is None:
            chromosome = Chromosome(chromosomeName)
            chromosomeDict[chromosomeName] = chromosome
        
        snp = SNP(refAllele, altAllele, snpId, snpPosition, chromosomeName)
        
        chromosome.addSNP(snp)
        
    for key in chromosomeDict.keys():
        chromosome = chromosomeDict[key]
        
        transitions = chromosome.count_transitions()
        print("# of transitions for " + chromosome.getName() + " = " + str(transitions))
        