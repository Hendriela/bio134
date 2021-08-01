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

# Ana 1
def to_fasta(filename):
    fyle = open(filename)
    dd = fyle.readlines()
    fyle.close()

    iterations = 1000000
    time1 = time.time()

    for i in range(iterations):

        new = []

        # Introduce new variable that keeps track if we are past "ORIGIN" in the Genbank file
        saw_origin = False

        for line in dd:
            # Test if we already saw "ORIGIN" (this would mean we have to start processing the string)
            if saw_origin:
                # If we did, we process the line with your code (which works) and append the modified line to "new"
                line = line.strip()
                line = line.strip("//123456789")
                line = ''.join(line.split())
                new.append(line.upper())
            # If "ORIGIN" is the current line, we set our saw_origin variable to "True" to remember it, and start processing
            # the string in the next for-loop round (the following line). Also, we start to create the content of our new
            # text file by creating the header.
            if 'ORIGIN' in line:
                saw_origin = True
                new.append('>header')

        # If we want to be precise, we have to remove the last element of "new". The last element is an empty string due to
        # the last line in the Genbank file being "//", which we strip away, leaving an empty string. This is not 100%
        # required imo, because if you leave it in, you will just have an unnecessary line break at the end of the document
        new = new[:-1]

        # Join the lines together with "\n" as a separator to keep lines separated by line breaks (this is necessary because
        # you can only write strings into a text file, not lists).
        new_content = '\n'.join(new)

    time2 = time.time()
    time_per_it = (time2-time1)
    print('{:f} micro seconds'.format(time_per_it))

    # Get the new filename by getting the protein ID from the Genbank filename (split at the dot) and add fasta to it
    filename_fasta = filename.split('.')[0] + '.fasta.txt'

    # Create a new text file with the new filename. If the file does not exist, Python automatically creates it,
    # otherwise the existing file with the same name gets overwritten
    fyle = open(filename_fasta, 'w')
    # Write the content string to the file and close it
    fyle.write(new_content)
    fyle.close()

    # If you want to have access to the new content in Python, you can return it here, but this is not required for the
    # exercise (the file gets saved anyway, independently from the return)
    return new_content

# Ana
def to_fasta(filename):
    fyle = open(filename)
    dd = fyle.readlines()
    fyle.close()


    iterations = 1000000
    time1 = time.time()

    for i in range(iterations):
        new = []
        # Here, we first join the lines to one big string, so that we can use the "partition()" function to split the string
        # at our keyword "ORIGIN" and only keep the parts after it. Then we split the string into lines again so that we can
        # format them with your code.
        dd_join = ''.join(dd)
        seq = dd_join.partition('ORIGIN')[2]
        lines = seq.split('\n')

        # In the previous version we removed the last line ("//") afterwards, but we can also just exclude it from the loop.
        # We can do this because in all Genbank files "//" (which we have to remove) is the last line, so this solution is
        # still general.
        for line in lines[:-1]:
            line = line.strip()
            line = line.strip("//123456789")
            line = ''.join(line.split())
            new.append(line)

        # Join the lines together with "\n" as a separator to keep lines separated by line breaks (this is necessary because
        # you can only write strings into a text file, not lists).
        new_content = '\n'.join(new)

        # FASTA files have the amino acids in upper case
        new_content = new_content.upper()

        # In the previous version we created the header during the for-loop, here we have to do it afterwards
        new_content = '>header' + new_content
    time2 = time.time()
    time_per_it = (time2-time1)
    print('{:f} micro seconds'.format(time_per_it))


    # The rest is the same as the previous version
    filename_fasta = filename.split('.')[0] + '.fasta.txt'
    fyle = open(filename_fasta, 'w')
    fyle.write(new_content)
    fyle.close()

    return new_content

A = to_fasta("P42677.genbank.txt")
print(A)
print(A[3])

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

