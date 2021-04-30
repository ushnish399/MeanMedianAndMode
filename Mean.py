import csv
with open("../DataSets/SOCR-HeightWeight.csv", newline="")as f: 
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    newdata.append(float(num))

n=len(newdata)
sum=0
for x in newdata:
    sum=sum+x

mean=sum/n
print(mean)
