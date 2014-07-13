GFF-Parser
==========

GFF parser for maize genomics. 

General Feature Format (GFF) also known as Gene-Finding Format is a file format which describes the features of genomic and protein sequences. A GFF file is a tab delimited text file where each feature is described on a single line. 
More information about GFF format can be found at <a href="http://www.sanger.ac.uk/resources/software/gff/">Wellcome Trust Sanger Institute</a>.

For maize, the GFF file I used looks like - 
9	ensembl	chromosome	1	156750706	.	.	.	ID=9;Name=chromosome:AGPv2:9:1:156750706:1
9	ensembl	gene	66347	68582	.	-	.	ID=GRMZM2G354611;Name=GRMZM2G354611;biotype=protein_coding
9	ensembl	mRNA	66347	68582	.	-	.	ID=GRMZM2G354611_T01;Parent=GRMZM2G354611;Name=GRMZM2G354611_T01;biotype=protein_coding
9	ensembl	intron	68433	68561	.	-	.	Parent=GRMZM2G354611_T01;Name=intron.1


