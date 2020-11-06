#%% Functions

def test_square(a, b):
    if a**2 < b:
        print("the square of", a, "is smaller than", b)
    else:
        print("the square of", a, "is not smaller than", b)
print(test_square(4, 17))


#%% Genbank

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



def fasta_to_genbank_Julian(filename):
    # Load file
    with open(filename) as f:
        fasta = f.readlines()
        SEQ = []
        header = False
        for line in fasta:
            if header == False:
                SEQ.append('>header')
                header = True
            else:
                line = line.lower()
                for i, el in enumerate(line):
                    if i%60 == 0:
                        SEQ.append(i-59)
                    if i%10 == 0:
                        SEQ.append(line[i - 9:i])
    print(SEQ)

