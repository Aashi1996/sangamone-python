country=[]
lat=[]
lon=[]
latValue=[]
lonValue=[]
patientLocation=['28.5383','81.3792']
a=57.29577951  #PI/180
m=3963
#d=ACOS( SIN(lat1*PI()/180)*SIN(lat2*PI()/180) + COS(lat1*PI()/180)*COS(lat2*PI()/180)
# *COS(lon2*PI()/180-lon1*PI()/180))* 6371000
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

