#%% Lists

lys = ['j', 'm', 'd', 'e', 'j', 'm', 'c', 'b', 't', 'v', 'a', 'w', 'p', 'c', 'q', 's', 'x', 'f', 'p', 'u', 'j', 'x',
       'c', 'w', 'x', 'q', 'l', 'w', 'r', 'j', 'm', 'f', 't', 'x', 'a', 'o', 's', 'n', 'a', 'g', 'm', 'd', 'a', 'd',
       'b', 'o', 'p', 'i', 'o', 'x', 'n', 'k', 'w', 'x', 'd', 'u', 'a', 'd', 'r', 'k', 'f', 'g', 'g', 'f', 'a', 'v',
       'v', 'f', 's', 'w', 'g', 'l', 'k', 'y', 'd', 'm', 'z', 'k', 'e', 'r', 't', 'x']
dna = ['a', 't', 'c', 'g']
rna = ['a', 'u', 'c', 'g']
lys_dna = lys.copy()
lys_rna = lys.copy()

for i in range(len(lys)):
    if lys[i] not in dna:
        lys_dna.remove(lys[i])
    if lys[i] not in rna:
        lys_rna.remove(lys[i])



lista = ['y', 'w', 'i', 'c', 'o', 'e', 'f', 'z', 'p', 'v', 'q', 'k', 'p', 'j', 'p', 's', 'j', 'n', 'q', 'z', 'x', 'r',
         'r', 'n', 'x', 'g', 'g', 's', 'y', 'p', 'd', 't', 'c', 'a', 'b', 't', 'l', 'k', 'c', 'p', 'g', 'd', 'f', 'r',
         'x', 'n', 'm', 'f', 'b', 'm', 'z', 'j', 'u', 'g', 's', 'k', 'v', 'm', 'o', 'd', 'h', 'h', 'r', 'q', 'b', 'm',
         'v', 'w', 'q', 'x', 'g', 'k', 'p', 'e', 't', 'r', 'w', 'f', 'g', 'g']
dna=['a', 't', 'c', 'g']
rna=['a', 'u', 'c', 'g']
dnaL=[]
rnaL= []

for i in lista:
    if i in dna:
        dnaL.append(i)
    if i in rna:
        rnaL.append(i)
dnaL.sort()
rnaL.sort()
if len(dnaL) > len(rnaL):
    print(dnaL)
else:
    print (rnaL)

l = [['1', '5', '6'], ['8', '1'], ['5', '4', '4', '2']]
for el in l:
    el[0] = int(el[0])
print(l)

    for s in range(len(el)):
        el[s] = int(el[s])
print(l)

