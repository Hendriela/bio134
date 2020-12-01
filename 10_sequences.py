#%% Fetch protein sequences
from Bio import ExPASy, SeqIO
import matplotlib.pyplot as plt
p = __import__('10_pairs')
dp = __import__('10_dotplots')

#this function fetches a genbank file (sid = sequence ID) from Uniprot
def fetch_genbank(sid):
    try:
        handle = ExPASy.get_sprot_raw(sid)
        seq = SeqIO.read(handle,'swiss')
        SeqIO.write(seq, sid+'.genbank','genbank')
        print(sid,'sequence length',len(seq))
    except Exception:
        print (sid,'not found')

#this function extracts the organism name and the sequence
#from a local genbank file
def read_genbank_no_bio(sid):
    fyle = open(sid + '.genbank')
    l_fyle = fyle.readlines()
    fyle.close()

    l_seq = []
    found_origin = 0
    for line in l_fyle:
        if 'ORGANISM' in line:
            organism = ' '.join(line.split()[1:])
        if found_origin:
            l_seq.append(line)
        if 'ORIGIN' in line:
            found_origin = 1

    seq = ''
    for line in l_seq:
        seq += ''.join(line.strip().split()[1:]).upper()
    seq = seq.strip()
    return (organism, seq)

ids = ['P00846', 'Q95A26', 'Q9T9W0', 'Q2I3G9', 'Q9TA24']
for i in ids:
    fetch_genbank(i)

# Load sequences
data = []
for i in ids:
    data.append(read_genbank_no_bio(i))

# Make pairs
pairs = p.make_pairs(data)

# Compute dotplot coordinates
coords = []
width = 10
for pair in pairs:
    x, y = dp.match(pair[0][1], pair[1][1], width)
    coords.append((pair[0][0], pair[1][0], x, y))

# Autochecker test 1 (Human vs african elephant)
target1 = 'Human'
target2 = 'African elephant'
for pair in coords:
    if (target1 in pair[0] or target1 in pair[1]) and (target2 in pair[0] or target2 in pair[1]):
        print(sorted(zip(pair[2],pair[3]))[2])

# Autochecker test 2
# Chimp vs Orangutan
target1 = 'Chimpanzee'
target2 = 'orangutan'
for pair in coords:
    if (target1 in pair[0] or target1 in pair[1]) and (target2 in pair[0] or target2 in pair[1]):
        print(len(pair[2]))

# Total number of all species
matches = 0
for pair in coords:
    matches += len(pair[2])
print(matches)

# Autochecker test 3 (Closely related species)
max_pairs = ('species1', 'species2', 0)
for pair in coords:
    if len(pair[2]) > max_pairs[2]:
        max_pairs = (pair[0], pair[1], len(pair[2]))
print(max_pairs)

# Autochecker test 4 (longest sequence, plotting)
fig, axes = plt.subplots(2,5)
for idx, ax in enumerate(axes.ravel()):
    plt.sca(ax)
    name1 = coords[idx][0]
    name2 = coords[idx][1]
    pair_x = coords[idx][2]
    pair_y = coords[idx][3]
    dp.plot(pair_x, pair_y, name1, name2, width)

s = 'Linda,Mark,Nathan,Daniela'
lys = s.split(',')
print(lys)
['Linda', 'Mark', 'Nathan', 'Daniela']