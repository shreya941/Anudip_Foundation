students = [
    ["Name ","   email    ","attendance","CGPA"],
    ["Aarav", "aarav@example.com", 75, 8.3],
    ["Vihaan", "vihaan@example.com", 62, 6.1],
    ["Vivaan", "vivaan@example.com", 68, 7.2],
    ["Ananya", "ananya@example.com", 45, 3.5],
    ["Diya", "diya@example.com", 70, 7.9],
    ["Ishaan", "ishaan@example.com", 35, 2.8],
    ["Sara", "sara@example.com", 78, 8.7],
    ["Rohan", "rohan@example.com", 72, 7.5],
    ["Arya", "arya@example.com", 60, 6.4],
    ["Aditi", "aditi@example.com", 69, 7.1],
    ["Kavya", "kavya@example.com", 74, 7.8],
    ["Arjun", "arjun@example.com", 40, 3.2],
    ["Mira", "mira@example.com", 73, 7.6],
    ["Reyansh", "reyansh@example.com", 77, 8.4],
    ["Sneha", "sneha@example.com", 54, 5.0],
    ["Ayaan", "ayaan@example.com", 79, 8.9],
    ["Ira", "ira@example.com", 59, 6.3],
    ["Nisha", "nisha@example.com", 29, 2.4],
    ["Karan", "karan@example.com", 63, 6.5],
    ["Tanvi", "tanvi@example.com", 21, 2.1],
    ["Sahil", "sahil@example.com", 55, 5.2],
    ["Priya", "priya@example.com", 68, 7.3],
    ["Riya", "riya@example.com", 72, 7.5],
    ["Krishna", "krishna@example.com", 32, 3.0],
    ["Neha", "neha@example.com", 48, 4.2],
    ["Laksh", "laksh@example.com", 75, 8.0],
    ["Kunal", "kunal@example.com", 67, 7.0],
    ["Pooja", "pooja@example.com", 41, 3.6],
    ["Tara", "tara@example.com", 58, 5.9],
    ["Aakash", "aakash@example.com", 70, 7.8],
    ["Aakashi", "aakashi@example.com", 40, 3.4],
    ["Aaka", "aaka@example.com", 60, 6.0],
    ["kash", "kash@example.com", 13, 2.0],
    ["Aash", "aash@example.com", 20, 2.2],
    ["reshu", "reshu@example.com", 70, 7.9],
    ["shreya", "shreya@example.com", 70, 7.8]
]

#print(students)

#count=0
#for x in students:
#    if x[2]>50:
#        count+=1
#print(count)
#for x in students:
#    print(*x)

#list1=list([1,2,3])
#for i in list1:
#    print(i," ",end=" ")  
#print(*list1)



#SLICING OPERATION------------------------------------------
#list2=[1,2,3,4,5,6,7,8,9]
#print("3rd element from start",list2[2])
#print("4th element from last ", list2[-4])
#print("elements between 3rd and 8th position",list2[2:8])

#list3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#print(*list3[19:0:-1],end=" ")
#print(list3[0])

#x=20
#while(x>0):
#    print(x,end=" ")
#    x-=1 




#using insertion-----------------------------------------------------

#list4=[1,2,3,4]
#print(list4)
#list4.append(3)
#print("using append : ",list4)
#list4.extend([5,6,7])
#print("using extend : ",list4)
#list4.insert(2,7)
#print("using insert : ",list4)

#my_list = [3, 4, 4, 5, 6]
#elements_to_insert = [9, 8, 7]
#index = 2

# Use slicing and sum function to insert elements one by one
#my_list = my_list[:index] + elements_to_insert + my_list[index:]
#print(my_list)

#REMOVING DATA ----------------------------------------------------

#usin pop method--we pass index as an argument

list5=[1,7,7,8,2,3,4,5,6,7,8,9]
print("before removing : ",list5)
list5.pop(4)
list5.pop()
print("after poping ",list5)

#using remove function--in this we pass element as an argument, generates exception if element is not present

list5.remove(7)
print("after removing ",list5)

#using clear() -to delete all the elements from list

list5.clear()
print("after clearing", list5)
