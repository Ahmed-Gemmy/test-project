from read import SeqRead

file_path = r'E:\example\ERR2660561.fastq'
counter = 1

reads = []

with open(file_path) as f:
    while True:
        lines = []
        for i in range(4):
            lines.append(next(f))
            counter += 1

        reads.append(SeqRead(seq=lines[1], read_id=lines[0], qualit=lines[3]))
        if counter >= 50:
            break

for read in reads:
    print('{read_id}: has sequence of {read_len} bases'.format(read_id=read.id.strip(), read_len=read.get_seq_len()))
    print(read.get_bases_quality())
    print('=' * 30)

