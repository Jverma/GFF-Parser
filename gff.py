## Parsing gff file to extract data to be used for other purposes.
## Author - Janu Verma
## jv367@cornell.edu


import sys



class parser:
    """
    GFF Parser Class.
    Extracts the relevant information and stores it in a way which facilitates quick access and processing.
    """
    def __init__(self, input_file):
        self.data = {}
        self.dict = {}
        for line in input_file:
            record = line.strip().split("\t")
            sequence_name = record[0]
            source = record[1]
            feature = record[2]
            start = int(record[3])
            end = int(record[4])
            if (record[5] != '.'):
                score = record[5]
            else:
                score = None
            if (record[6] == '+'):
                strand = 1
            else:
                strand = -1
            if (record[7] != '.'):
                frame = record[7]
            else:
                frame = None
            attributes = record[8].split(';')
            attributes = {x.split('=')[0] : x.split('=')[1] for x in attributes if '=' in x}
            if not(sequence_name in self.data):self.data[sequence_name] = []
            alpha = {'source':source, 'feature':feature, 'start':start, 'end':end, 'score':score, 'strand':strand, 'frame':frame}
            for k,v in attributes.iteritems(): alpha[k] = v
            self.data[sequence_name].append(alpha)

    def geneDict(self):
        """
        Creates a dictionary of all the genes in the file.
        Returns : 
        A dictionary with gene names as keys and the corresponding chromosome number as value.
        """
        allGenes = {}
        for x in self.data:
            y = self.data[x]
            for z in y:
                if (z['feature'] == 'gene'):
                    name_of_gene = z['Name']
                    allGenes[name_of_gene] = x
        return allGenes
    

    def getGenes(self, Id):
        """
        Gets all the genes for a chromosomes with all the relevant information. 
        Arguments : 
        Id -- The identifier for the sequence. e.g. 9, 1, 2 in our file. 
        
        Returns :
        A list of dictionaries where each dictionary corresponds to a gene in the sequence.
        """
        genes_list = []
        chromosome = self.data[Id]
        for x in chromosome:
            if (x['feature'] == 'gene'):
                gene_info = {'Id': x['ID'], 'source': x['source'],'start': x['start'], 'end': x['end'], 'score': x['score'], 'strand': x['strand'], 'frame': x['frame']}
                genes_list.append(gene_info)
        return genes_list


    def get_mRNA(self,seq_name, Id):
        """
        Gets all the mRNAs (transcripts) for a given gene. 
        Arguments : 
        seq_name -- The name/identifier of the sequence.
        Id -- The identifier/name of the gene we are interested in. 
        
        Returns : 
        A list of dictionaries where each dictionary contains information about an mRNA for the gene.
        """
        mRNA_list = []
        for x in self.data[seq_name]:
            if (x['feature'] == 'mRNA') and (x['Parent'] == Id):
                mRNA_info = {'Id': x['ID'], 'source': x['source'],'start': x['start'], 'end': x['end'], 'score': x['score'], 'strand': x['strand'], 'frame': x['frame']}
                mRNA_list.append(mRNA_info)
        return mRNA_list


    def getIntrons(self, seq_name, Id):
        """
        Gets all the introns for a given transcript (mRNA). 
        Arguments : 
        seq_name -- Name of the sequence.
        Id -- Identifier of the mRNA. 
        
        Returns : 
        A list of dictionaries where each dictionary contains the informations about an intron for the transcript.
        """
        intron_list = []
        for x in self.data[seq_name]:
            if (x['feature'] == 'intron') and (x['Parent'] == Id):
                intron_info =  {'Name': x['Name'],'start': x['start'], 'end': x['end'], 'score': x['score'],'frame': x['frame']}
                intron_list.append(intron_info)
        return intron_list


    def getExons(self, seq_name, Id):
        """
        Gets all the exons for a given transcript (mRNA).
        Arguments :
        seq_name -- Name of the sequence.
        Id -- Identifier of the mRNA.
        
        Returns :
        A list of dictionaries where each dictionary contains the informations about an exon for the transcript.
        """
        exon_list = []
        for x in self.data[seq_name]:
            if (x['feature'] == 'exon') and (x['Parent'] == Id):
                exon_info =  {'Name': x['Name'],'start': x['start'], 'end': x['end'], 'score': x['score'],'frame': x['frame']}
                exon_list.append(exon_info)
        return exon_list


    def getCDS(self, seq_name, Id):
        """
        Gets all the CDS for a given transcript (mRNA).
        Arguments :
        seq_name -- Name of the sequence.
        Id -- Identifier of the mRNA.
        
        Returns :
        A list of dictionaries where each dictionary contains the informations about an CDS for the transcript.
        """
        cds_list = []
        for x in self.data[seq_name]:
            if (x['feature'] == 'CDS') and (x['Parent'] == Id):
                cds_info =  {'Name': x['Name'],'start': x['start'], 'end': x['end'], 'score': x['score'],'frame': x['frame']}
                cds_list.append(cds_info)
        return cds_list




