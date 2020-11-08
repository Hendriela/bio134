#%% Functions
import time

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
    fyle_fasta = open(filename)
    # fyle_genbank = open(filename.split('.')[0] + '.genbank.txt', 'w')
    list_fasta = fyle_fasta.readlines()[1:]
    s = 'ORIGIN\n'
    number = 1
    for line in list_fasta:
        line = line.strip().lower()
        s += '{:9d}'.format(number)
        for i in range(0, 60, 10):
            if len(line[i:i+10]) > 0:
                s += ' '+line[i:i+10]
                print(line[i:i+10])
            else:
                print('here')
        s += '\n'
        number += 60
    s += '//'
    print(s)

# -*- coding: utf-8 -*-

def fasta_to_genbank_sol(sid):
    fyle_fasta = open(sid + '.fasta.txt')
    fyle_genbank = open(sid + '.genbank.txt', 'w')
    list_fasta = fyle_fasta.readlines()[1:]

    iterations = 1000000
    time1 = time.time()
    for k in range(iterations):
        s = 'dummy header\nORIGIN\n'
        number = 1
        for line in list_fasta:
            line = line.strip().lower()
            s += '{:9d}'.format(number)
            for i in range(0, 60, 10):
                if len(line[i:i+10])>0:
                    s += ' '+line[i:i+10]
            s += '\n'
            number += 60
        s += '//'
    time2 = time.time()
    time_per_it = (time2-time1)
    print('{:f} micro seconds'.format(time_per_it))
    print(s)

    print(s)
    fyle_genbank.write(s)
    fyle_fasta.close()
    fyle_genbank.close()

fasta_to_genbank('B4F440')

