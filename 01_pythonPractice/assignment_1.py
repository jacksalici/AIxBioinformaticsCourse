"""Assignment 1: Statistics extraction 
    
Write  a  python  program  for  extracting  statistics  from  fasta/fastq  files.  The  program  must  take  as  a  first 
argument from the command line the name of the input fasta file to be analyzed and write to an output text 
file  (whose  name  is  passed  as  a  second  argument  from  the  command  line)  a  summary  of  the  computed 
statistics. 
The following are the expected output statistics: 
- Statistics of single bases across all the reads: Number of A,T,C,G 
- Number of reads having at least one low complexity sequence: AAAAAA, TTTTTT, CCCCCC or GGGGGG. 
-  Number  of  reads  having  the  number  of  GC  couples  (so  called  GC  content)  higher  than  a  threshold 
GC_THRESHOLD passed as third argument from the command line 
- For each read having a GC content higher than GC_THRESHOLD, report  the read_id and the number of GC 
couples
"""



import sys

bases = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}
low_complexity_sequences = {'AAAAAA' : 0, 'TTTTTT' : 0, 'CCCCCC' : 0, 'GGGGGG' : 0}
gc_content_number = 0


with open(sys.argv[1]) as file:
    for index, line in enumerate(file.readlines()[1::2]):
        
        #Statistics of single bases across all the reads: Number of A,T,C,G
        for base in bases.keys():
            bases[base]+=line.count(base)
        
        #Number of reads having at least one low complexity sequence: AAAAAA, TTTTTT, CCCCCC or GGGGGG.
        for sequence in low_complexity_sequences.keys():
            if sequence in line:
                low_complexity_sequences[sequence]+=1
        
        # Number  of  reads  having  the  number  of  GC  couples  (so  called  GC  content)  higher  than  a  threshold  GC_THRESHOLD passed as third argument from the command line
        if line.count('GC') > int(sys.argv[2]):
            gc_content_number+=1
            
            # For each read having a GC content higher than GC_THRESHOLD, report  the read_id and the number of GC couples 
            
            print(f'Read {index} has the GC content higher than the threshold.')
 
            
print('Number of bases found across the reads: ' + str(bases))      
print('Number of reads with at least one low complexity sequence: ' + str(low_complexity_sequences))
print('Total number of reads with GC countent higer of the threshold: ' + str(gc_content_number))