names=[]
subjects=[]
eng=[]
engToppers=[]
maths=[]
mathsToppers=[]
phy=[]
phyToppers=[]
chem=[]
chemToppers=[]
bio=[]
bioToppers=[]
totalMarks=[]
topper=[]

f1=open("Marks.txt","r")
for i in range(0,26,1):
    
    info=f1.readline()
    list1=info.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    subjects.append(list2[0])
    eng.append(list2[1])
    
    list2=list1[4].split(":")
    subjects.append(list2[0])
    maths.append(list2[1])
    
    list2=list1[5].split(":")
    subjects.append(list2[0])
    phy.append(list2[1])
    
    list2=list1[6].split(":")
    subjects.append(list2[0])
    chem.append(list2[1])
    
    list2=list1[7].split(":")
    subjects.append(list2[0])
    bio.append(list2[1])

print(names)
print(eng)
print(maths)
print(phy)
print(chem)
print(bio)
print()

maxEng=max(int(i)for i in eng)
maxMaths=max(int(i) for i in maths)
maxPhy=max(int(i) for i in phy)
maxChem=max(int(i) for i in chem)
maxBio=max(int(i) for i in bio)
print()

print("Max of English Marks is:",maxEng)
print("Max of Maths Marks is:",maxMaths)
print("Max of Physics Marks is:",maxPhy)
print("Max of Chemistry Marks is:",maxChem)
print("Max of Biology Marks is:",maxBio)
print()

for i in range(0,26,1):
    if int(eng[i])==maxEng:
        engToppers.append(names[i])
print(engToppers,"are the toppers in", subjects[0], "with marks of",maxEng)

for i in range(0,26,1):
    if int(maths[i])==maxMaths:
        mathsToppers.append(names[i])
print(mathsToppers,"are the toppers in", subjects[1], "with marks of",maxMaths)

for i in range(0,26,1):
    if int(phy[i])==maxPhy:
        phyToppers.append(names[i])
print(phyToppers,"are the toppers in", subjects[2], "with marks of",maxPhy)

for i in range(0,26,1):
    if int(chem[i])==maxChem:
        chemToppers.append(names[i])
print(chemToppers,"is the topper in", subjects[3], "with marks of",maxChem)

for i in range(0,26,1):
    if int(bio[i])==maxBio:
        bioToppers.append(names[i])
print(bioToppers,"are the toppers in", subjects[4], "with marks of",maxBio)
print()

for i in range(0,26,1):
    totalMarks.append(int(eng[i])+int(maths[i])+int(phy[i])+int(chem[i])+int(bio[i]))
print(totalMarks)
print()

maxTotal=max(int(i) for i in totalMarks)
print("Max of Total Marks is:",maxTotal)
print()

for i in range(0,26,1):
    if int(totalMarks[i])==maxTotal:
        topper.append(names[i])
print(topper,"is the Gold Medalist with total marks of",maxTotal)

