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
maxEng=max(eng)
maxMaths=max(maths)
maxPhy=max(phy)
maxChem=max(chem)
maxBio=max(bio)
print(maxEng)
print(maxMaths)
print(maxPhy)
print(maxChem)
print(maxBio)

for i in range(0,26,1):
    if eng[i]==maxEng:
        engToppers.append(names[i])
print(engToppers,"are the toppers in", subjects[0], "with marks of",maxEng)

for i in range(0,26,1):
    if maths[i]==maxMaths:
        mathsToppers.append(names[i])
print(mathsToppers,"are the toppers in", subjects[1], "with marks of",maxMaths)

for i in range(0,26,1):
    if phy[i]==maxPhy:
        phyToppers.append(names[i])
print(phyToppers,"are the toppers in", subjects[2], "with marks of",maxPhy)

for i in range(0,26,1):
    if chem[i]==maxChem:
        chemToppers.append(names[i])
print(chemToppers,"is the topper in", subjects[3], "with marks of",maxChem)

for i in range(0,26,1):
    if bio[i]==maxBio:
        bioToppers.append(names[i])
print(bioToppers,"is the topper in", subjects[4], "with marks of",maxBio)

x=sum(eng[0],maths[0])
