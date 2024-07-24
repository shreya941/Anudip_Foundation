#file handling in csv files
import csv
f=open("hell.csv",'a',newline='')
w=csv.writer(f)
data=[[1,2,3,4],[4,5,6,7],[8,9,10,11]]
w.writerow(data)
w.writerows(data)
f.close()
