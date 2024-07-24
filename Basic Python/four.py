import pandas as pd
students = [
    {"stdid": "std101", "stdname": "Ashish Kumar", "standard": "10th", "Age": 15, "Hindi": 89, "English": 67, "Maths": 87, "Science": 89, "Computer": 90, "Total": 422},
    {"stdid": "std102", "stdname": "Abhishek Kumar", "standard": "10th", "Age": 14, "Hindi": 45, "English": 85, "Maths": 60, "Science": 87, "Computer": 50, "Total": 313},
    {"stdid": "std103", "stdname": "Aman", "standard": "10th", "Age": 14, "Hindi": 90, "English": 45, "Maths": 89, "Science": 45, "Computer": 90, "Total": 359},
    {"stdid": "std104", "stdname": "Rahul", "standard": "10th", "Age": 15, "Hindi": 67, "English": 78, "Maths": 67, "Science": 78, "Computer": 56, "Total": 302},
    {"stdid": "std105", "stdname": "Ruby", "standard": "10th", "Age": 14, "Hindi": 78, "English": 89, "Maths": 78, "Science": 89, "Computer": 67, "Total": 403},
    {"stdid": "std106", "stdname": "Suman", "standard": "10th", "Age": 13, "Hindi": 56, "English": 56, "Maths": 49, "Science": 56, "Computer": 78, "Total": 295},
    {"stdid": "std107", "stdname": "Saurabh", "standard": "10th", "Age": 15, "Hindi": 34, "English": 35, "Maths": 67, "Science": 34, "Computer": 45, "Total": 215},
    {"stdid": "std108", "stdname": "Sumit", "standard": "10th", "Age": 14, "Hindi": 57, "English": 78, "Maths": 89, "Science": 78, "Computer": 67, "Total": 369},
    {"stdid": "std109", "stdname": "Kamlesh", "standard": "10th", "Age": 14, "Hindi": 67, "English": 34, "Maths": 56, "Science": 67, "Computer": 45, "Total": 345},
    {"stdid": "std110", "stdname": "Rohan", "standard": "10th", "Age": 15, "Hindi": 24, "English": 34, "Maths": 45, "Science": 24, "Computer": 56, "Total": 171}
]


# Create a DataFrame
df = pd.DataFrame(students)

# Display the DataFrame
print(df)
print("_________________________________________________________________________")
#print name students who have scored more than 50 in english
for x in students:
    if x["English"]>50:
        print("student :" , x["stdname"])

print("_________________________________________________________________________")
#print id name and marks of students who are bottom 3 in computer
list1=sorted(students,key=lambda x: x["Computer"])  

j=0
for i in list1:
    if j<3:
        print(i["stdid"],i["stdname"],i["Computer"])
        j+=1

        
print("___________________________________________________________________________")
#print id name and marks of students who are top 3 in maths
list2=sorted(students,key=lambda x: x["Maths"], reverse=True)
k=0
for i in list2:
    if k<3:
        print(i["stdid"],i["stdname"],i["Maths"])
        k+=1
print(" ______________________________________________________________________________")
#slicing operations in tuple
tup=(1,2,3,4,5)
print(tup[4:0:-1])


#DICTIONARYYYYYYYYYYY
dict1={}
dict1["name"]="shreya"
dict1["age"]=21
print(dict1)
for key in dict1:
    print(key, " - ",dict1[key])
