country=[]
lat=[]
lon=[]
latValue=[]
lonValue=[]
patientLocation=['28.5383','81.3792']
d=[]
nearestCentre=[]

f1=open("location.txt","r")
for i in range(0,4,1):
    info=f1.readline()
    list1=info.split(":")
    country.append(list1[0])
    list2=list1[1].split(",")
    lat.append(list2[0])
    lon.append(list2[1])
    list3=list2[0].split("Ã")
    list4=list2[1].split("Ã")
    latValue.append(list3[0])
    lonValue.append(list4[0])
print(country)
print(lat)
print(lon)
print(latValue)
print(lonValue)
print(patientLocation[0])
print()

import math
for i in range(0,4,1):
    d.append(math.sqrt(float(float(patientLocation[0])-float(latValue[i]))**2)+float(float(patientLocation[1])-float(lonValue[i]))**2)
print(d)
print()

minDist=min(float(i) for i in d)
for i in range(0,4,1):
    if(float(d[i]))==minDist:
        nearestCentre.append(country[i])
print(nearestCentre,"is the nearest centre for covid testing with distance of:",minDist)
