
def genbank_to_fasta(filename):

    # Load file
    with open(filename) as f:
        genbank = f.readlines()

    saw_origin = False
    seq = []
    for line in genbank:
        if saw_origin:
            seq.append(''.join(line.strip().split(' ')[1:]).upper() + '\n')
        if 'ORIGIN' in line:
            saw_origin = True
            seq.append('>header\n')

    seq = seq[:-1]
    seq[-1] = seq[-1].strip()

    filename_new = filename.split('.')[0] + '.fasta.txt'
    with open(filename_new, 'w') as f:
        f.write(''.join(seq))


def fasta_to_genbank(filename):
    with open(filename) as f:
        fasta = f.read()

    seq = ''.join(fasta.partition('\n')[2].split('\n'))
    seq = seq.lower()

    genbank = ''

    for i in range(0, len(seq), 10):
        if i % 60 == 0:
            genbank += '\n{:9d}'.format(i+1)
        genbank += ' ' + seq[i:i+10]


    header = filename.split('.')[0] + '\nORIGIN'
    content = header + genbank + '\n//'
    # adapt new file name
    filename_new = filename.split('.')[0] + '.genbank.txt'

    with open(filename_new, 'w') as f:
        f.write(content)

