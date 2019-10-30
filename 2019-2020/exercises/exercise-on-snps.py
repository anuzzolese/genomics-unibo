import csv
from abc import ABC, abstractclassmethod

'''
Abstract class for representing a general allele variation.
The abstract class provides two abstract method (not implemented by the astract class),
i.e. isTransition() and isTransition().
AlleleVariation can be said a CLASS INTERFACE as it is an abstrac class whose methods are all abstracts.
The distinction between abstract class and class interface is simple: a class interface is an abstract class
whose methods are all declared abstracts. We remenind that an abstract class can have some implemented method 
as it can be defined as a class having at least 1 abstract method.
'''
class AlleleVariation(ABC):
    
    '''
    We use the decorator @abstractclassmethod in order to allow Python to handle this method as abstract correctly.
    Additionally, we use "pass" as the method body in order to avoid any implmentation.
    '''
    @abstractclassmethod
    def isTransition(self):
        pass
    
    '''
    We use the decorator @abstractclassmethod in order to allow Python to handle this method as abstract correctly.
    Additionally, we use "pass" as the method body in order to avoid any implmentation.
    '''
    @abstractclassmethod
    def isTransversion(self):
        pass
        
'''
A SNP class hold relevant information about a single line in the VCF file. 
It is a concrete imlementation of the AlleleVariation, which in turn is an abstract class.

'''
class SNP(AlleleVariation):
    
    '''
    The constructor allows us to create individuals by setting actual values
    for the following private attributes:
      - the reference allele (a one-character string in column 4, e.g., “A”);
      - the alternative allele (a one-character string in column 5, e.g., “G");
      - the name of the chromosome on which it exists (a string in column 1, e.g., “1");
      - the reference position (an integer in column 2, e.g., 799739);
      - the ID of the SNP (in column 3, e.g., "rs57181708" or "."). 
    '''
    def __init__(self, refBase, altBase, snpId, snpPosition, chromosomeName):
        #the information in input should be store
        # as private attribute of class's individuals
        self.__refBase = refBase
        self.__altBase = altBase
        self.__snpId = snpId
        self.__snpPosition = snpPosition
        self.__chromosomeName = chromosomeName
    
    '''
    This is the concrete implementation of the AlleleVariation.isTransition() abstract method.
    The concrete implementationg is provided by means of overriding.
    In fact SNP.isTransition() overrides AlleleVariation.isTransition().
    The method return True if a transition is found, False otherwise.
    A transition is detected in any of the following cases, A/G, G/A, C/T, and T/C
    '''
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
        
    '''
    This is the concrete implementation of the AlleleVariation.isTransversion() abstract method.
    The concrete implementationg is provided by means of overriding.
    In fact SNP.isTransversion() overrides AlleleVariation.isTransversion().
    The following is a naïve implementation of isTransversion() that is implemented as the complement of
    the method SNP.isTransition(), i.e. if SNP.isTransition() returns False, then SNP.sTransversion() return True
    and, similarly, if SNP.isTransition() returns True, then SNP.sTransversion() return False.
    '''
    # A transversion is any case that is not a transition
    def isTransversion(self):
        return not self.isTransition()

'''
The following class implements a Chromosome that provides four methods: 
   - count_transitions(), which returns the number of transition SNPs
   - count_transversions(), which returns the number of transversion SNPs
   - addSNP(), which add a SNP object into the array of SNPs associated to the current Chromosome
   - getName, which returns the string representing the name of the Chromosome
'''
class Chromosome:
    
    '''
    A instance object of the Chromosome class is created by providing a name for
    the chromosome (e.g. 1, 2, or X) an by initialising an empty array that will be used later
    for storing SNPs that are read from the input dataset.
    '''
    def __init__(self, name):
        self.__name = name
        self.__snps = []
    
    '''
    The method count_transitions() returns the number of transition SNPs.

    '''
    def count_transitions(self):
    	''' We initialise the variable transitions to 0. 
    	Such a variable represents the counter of the number of transitions.
    	'''
        transitions = 0
        
        ''' Then we iterate the list of SNPs of the current chromosome. 
        If it is a transition we increment the value of the transitions counter.
        '''
        for snp in self.__snps:
            if snp.isTransition:
                transitions = transitions + 1
        
        return transitions
    
    '''
    TODO: The method count_transversions() returns the number of transverion SNPs.
    The implemantation shold follow the same solution adopted for count_transitions.
    '''
    def count_transversions(self):
        pass
    
    '''
    The followint method add an object of the class SNP to the list of snips owned by the current chromosome.
    The SNP is added at the end of the list, hence it is appended.
    '''
    def addSNP(self, snp):
        self.__snps.append(snp)
    
    '''
    The following method returns the name of the chromosome, e.g. 1, 2, or X.
    '''
    def getName(self):
        return self.__name
    
'''
We open the dataset that is represented by the file trio.sample.vcf.
The file is accessed by using the Python function open, that opens a file, and returns it as a file object.
The with statement in Python is used in exception handling to make the code cleaner and much more readable. 
More information about the the with statement can be found at https://www.geeksforgeeks.org/with-statement-in-python/.
'''   
with open('trio.sample.vcf') as csv_file:
    
    '''
    We read the input dataset as CSV file.
    This is done by usinf the reader prpvided by the Python csv module.
    We set the delimiter to the chareacter '\t' (tab) as the columns within the 
    dataset are separated by such a character.
    '''
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    
    '''
    We create the dictionary chromosomeDict.
    This dictionary is used for storying chromosome objects once created.
    Each chromosome object is associated in the dictionary with its name.
    Indeed the name is used as dictionary key.
    The dictionary is usefull as it allows to keep a reference to any of instace objects
    of the cass chromosome we create. Accordingly, we can:
     - create an instance of chromosome only once when we meet a new chromosome in the dataset and retrieving such an instance from the dictionary for its subsequent occurrences in the dataset;
     - add SNPs individuals to their correspoinding chromosomes when iterating the dataset.
    '''
    chromosomeDict = dict()
    
    '''
    We iterate the csv_reader, hence reading the dataset row by row.
    Each row is returned by the reader as an array of strings.
    '''
    for row in csv_reader:
    	'''
    	Thus we are able to retrieve the fowllowing data:
    	  - the chromosome name at position 0 of the array;
    	  - the SNP's position in the chromosome at position 1;
    	  - the SNP's ID at position 2;
    	  - the reference allele as available for the reference human genome at position 3;
    	  - the alternative allele as available for the trio analysis at position 4.
    	'''
        chromosomeName = row[0]
        snpPosition = row[1]
        snpId = row[2]
        refAllele = row[3]
        altAllele = row[4]
        
        '''
        When we read a row in the dataset we have a refernece to a chromosome.
        Then, we first check if an object representing such a chromosome exists 
        in the dictionary. If it exists we retrieve that isntace. Otherwise we
        create a new instance object and we store this instance in the dictionary.
        '''
        chromosome = chromosomeDict.get(chromosomeName, None)
        if chromosome is None:
            chromosome = Chromosome(chromosomeName)
            chromosomeDict[chromosomeName] = chromosome
        
        '''
        Now we create the object representing the SNP as it is read from the current
        row of the dataset.
        '''
        snp = SNP(refAllele, altAllele, snpId, snpPosition, chromosomeName)
        
        '''
        The we add the instance of SNP to the list of SNPs owned by its corresponding chromosome.
        '''
        chromosome.addSNP(snp)
        
    '''
    After all rows have been read, we iterate the chromosomes in the dictionary
    for printing their corresponding numbers of transitions and transversions.
    We iterate chromosomes in the dictionary by actually iterating dictionary's keys (i.e. chromosome names in our specific case)
    and then we use the keys for getting chromosome instances from the dictionary.
    '''
    for key in chromosomeDict.keys():
        chromosome = chromosomeDict[key]
        
        transitions = chromosome.count_transitions()
        print("# of transitions for " + chromosome.getName() + " = " + str(transitions))
        
