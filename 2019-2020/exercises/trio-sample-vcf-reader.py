import csv

if __name__ == '__main__':
    with open('trio.sample.vcf') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            chromosomeName = row[0]
            snpPosition = row[1]
            snpId = row[2]
            refAllele = row[3]
            altAllele = row[4]
            
            print(chromosomeName + ", " + snpPosition + ", " + snpId + ", " + refAllele + ", " + altAllele)