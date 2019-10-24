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
    
    def __init__(self, refAllele, altAllele, chromosome, position, snpId):
        self.__refAllele = refAllele
        self.__altAllele = altAllele
        self.__chromosome = chromosome
        self.__position = position
        self.__id = snpId
        
    
    def isTransition(self):
        if(self.__refAllele != self.__altAllele):
            if self.__refAllele == "A" or self.__refAllele == "G":
                if self.__altAllele == "A" or self.__altAllele == "G":
                    return True
                
            if self.__refAllele == "C" or self.__refAllele == "T":
                if self.__altAllele == "C" or self.__altAllele == "T":
                    return True
                
            return False
        else:
            return False
        
    
    def isTransversion(self):
        return not self.isTransition()
    
class Chromosome:
    
    def __init__(self, name):
        self.__name = name
        self.__snps = []
        
    def getName(self):
        return self.__name
        
    def addSNP(self, snp):
        if not isinstance(snp, SNP):
            raise TypeError("snp must be of type SNP.")
        else:
            self.__snps.append(snp)
            
    def countTransitions(self):
        transitions = 0
        for snp in self.__snps:
            if snp.isTransition():
                transitions = transitions + 1
                
        return transitions
    
    def countTransversion(self):
        transversions = 0
        for snp in self.__snps:
            if snp.isTransversion():
                transversions = transversions + 1
            
        return transversions


if __name__ == '__main__':
    chromosomes = dict()
    with open('trio.sample.vcf') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            chromosomeName = row[0]
            snpPosition = row[1]
            snpId = row[2]
            refAllele = row[3]
            altAllele = row[4]
            
            snp = SNP(refAllele, altAllele, chromosomeName, snpPosition, snpId)
            
            chromosome = chromosomes.get(chromosomeName, None)
            
            if chromosome is None:
                chromosome = Chromosome(chromosomeName)
                chromosomes[chromosomeName] = chromosome
            
            chromosome.addSNP(snp)
            
    for key in chromosomes.keys():
        chromosome = chromosomes[key]
        trans = chromosome.countTransitions()
        transv = chromosome.countTransversion()
        print(chromosome.getName() + " has " + str(trans) + " transitions and " + str(transv) + " transversions.")