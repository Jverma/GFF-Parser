## Parsing a fasta file to extract sequence information.
## Author - Janu Verma
## jv367@cornell.edu

import sys




class fastaExtract:
    """
    Extracts the sequence Id, chromosome number, parent_transcipt from the fasta files.
    """
    def __init__(self, fasta_files):
        self.data = {}
        self.seq_dict = {}
        for line in fasta_files:
            if (line[0] == '>'):
                line = line[1:]
                line = line.split(" ")
                self.data[line[0]] = []
                Id = line[0]
                self.seq_dict[Id] = ''
                Coord = line[2]
                Coord = Coord.split(":")
                Chromosome = Coord[0]
                Chromosome = Chromosome.split("=")
                self.data[line[0]].append(Chromosome[1])
                
                parent_transcript = line[3]
                parent_transcript = parent_transcript[:-1]
                parent_transcript = parent_transcript.split("=")
                self.data[line[0]].append(parent_transcript[1])

                parent_gene = line[4]
                parent_gene = parent_gene[:-1]
                parent_gene = parent_gene.split("=")
                self.data[line[0]].append(parent_gene[1])
                
                strand = Coord[2]
                self.data[line[0]].append(strand[:-1])
            
            else:
                line = line.strip()
                self.seq_dict[Id] = self.seq_dict[Id] + str(line)


    def getChromosomes(self):
        """
        Creates a dictionary of chromosome label for all the sequences in the file.
        Useful when we need to know the chromosome indetifier for a gene/mRNA sequence.
        
        Returns:
        A dictionary with sequence Id as the key and the chromosome number as the value.
        """
        chromo_dict = {}
        for x in self.data:
            chromo_dict[x] = self.data[x][0]
        return chromo_dict


    def getParent_transcript(self):
        """
        Creates a dictionary of parent transcripts for all the sequences in the file
            
        Returns:
        A dictionary with sequence Id as the key and the parent transcript as the value.
            """
        parent_dict = {}
        for x in self.data:
            parent_dict[x] = self.data[x][1]
        return parent_dict


    def getParent_gene(self):
        """
        Creates a dictionary of parent genes for all the sequences in the file.
        
        Returns:
        A dictionary with sequence Id as the key and the parent gene as the value.
        """
        gene_dict = {}
        for x in self.data:
            gene_dict[x] = self.data[x][2]
        return gene_dict


    def getStrand(self):
        """
        Creates a dictionary of strands for all the sequences in the file.
            
        Returns:
        A dictionary with sequence Id as the key and the strand as the value.
        """
        strand_dict = {}
        for x in self.data:
            strand_dict[x] = self.data[x][3]
        return strand_dict

    def getSequence(self):
        return self.seq_dict



